from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product, Batch
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.context import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """Handles payment checkout data and interfaces with Stripe."""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """Handles shipping data and interfaces with Stripe."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'eircode': request.POST['eircode'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    batch = Batch.objects.get(id=item_data['batch_id'])

                    order_line_item = OrderLineItem(
                        order=order,
                        batch=batch,
                        quantity=item_data['quantity'],
                    )
                    order_line_item.save()
                except Batch.DoesNotExist:
                    messages.error(request, (
                        "One of the batches in your \
                        bag wasn't found in our database. \
                        Please call us for assistance!"))
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request, "There was an error with your form."
                "Please double check your information."
            )
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                "bag": json.dumps(bag),
                "save_info": request.session.get("save_info", False),
                "username": (
                    request.user.username
                    if request.user.is_authenticated
                    else "AnonymousUser"
                ),
            }
        )

        order_form = None
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)

                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': request.user.email,
                    'phone_number': profile.default_phone_number,
                    'eircode': profile.default_eircode,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        if not order_form:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order.user_profile = profile
            order.save()

            if save_info:
                profile_data = {
                    'default_full_name': order.full_name,
                    'default_phone_number': order.phone_number,
                    'default_eircode': order.eircode,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                }
                user_profile_form = UserProfileForm(
                    profile_data, instance=profile)
                if user_profile_form.is_valid():
                    user_profile_form.save()

        except UserProfile.DoesNotExist:
            pass

    # Update stock after purchase
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        batch_id = item_data.get('batch_id')
        quantity = item_data.get('quantity', 0)
        name = item_data.get('name', '')

        try:
            batch = Batch.objects.get(id=batch_id)
            if batch.product.short_widget_name == name:
                batch.quantity -= quantity
                if batch.quantity < 0:
                    batch.quantity = 0
                batch.save()
        except Batch.DoesNotExist:
            pass

    messages.success(
        request,
        f'Order successfully processed! '
        f'Your order number is {order_number}. '
        f'A confirmation email will be sent to {order.email}.'
    )

    # Remove bag from the session
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
