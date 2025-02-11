from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Batch


def bag_contents(request):
    """Manages the bag contents"""
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, dict):
            product = get_object_or_404(Product, pk=item_id)

            batch = Batch.objects.filter(
                product=product, quantity__gt=0).order_by(
                    'expiry_date').first()
            if not batch:
                continue

            sale_price = batch.calculate_sale_price()
            total += item_data['quantity'] * sale_price
            product_count += item_data['quantity']
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data['quantity'],
                'product': product,
                'batch': batch,
                'price': sale_price,
                'name': item_data['name'],
            })
        else:
            product = get_object_or_404(Product, pk=item_id)

            batch = Batch.objects.filter(
                product=product, quantity__gt=0).order_by(
                    'expiry_date').first()
            if not batch:
                continue

            sale_price = batch.calculate_sale_price()
            total += item_data * sale_price
            product_count += item_data

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'batch': batch,
                'price': sale_price,
            })

    # Delivery Fee
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # Context
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
