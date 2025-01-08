from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from decimal import Decimal
from products.models import Product, Batch

# Create your views here.
def view_bag(request):
    """ A view that renders the cart contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified batch to the shopping cart """

    name = request.POST.get('name')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in bag:
        if isinstance(bag[item_id], dict):
            bag[item_id]['quantity'] += quantity
        elif isinstance(bag[item_id], int):
            bag[item_id] = {'quantity': bag[item_id] + quantity, 'name': name}
    else:
        bag[item_id] = {'quantity': quantity, 'name': name}

    request.session['bag'] = bag

    messages.success(request, f'Added {name} (x{quantity}) to your bag.')

    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    name = request.POST.get('name')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    max_quantity = request.POST.get('max_quantity') # Fetches the max from the form

    max_quantity = int(max_quantity)

    # Limits the user to update to only the max quantity avaible of the batch.
    if quantity > max_quantity:
        messages.error(request, f'Cannot add more than {max_quantity} units of {name}.')
        return redirect(reverse('view_bag'))

    if quantity > 0:
        bag[item_id] = {'quantity': quantity, 'name': name}
        messages.success(request, f'Updated size {name} quantity to (x{quantity})')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {name} quantity to (x{quantity})')

    print(bag)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        bag = request.session.get('bag', {})
        name = request.POST.get('name', 'item')

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {name} from your bag')
        else:
            messages.warning(request, 'Item not found in your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
