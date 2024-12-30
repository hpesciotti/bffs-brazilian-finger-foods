from django.shortcuts import render, get_object_or_404
from .models import Product, Batch

# Create your views here.

def all_products(request):
    """
    Returns all products and render main product page
    """

    products =  Product.objects.prefetch_related(
        'batches', 'dietary_categories'
    )

    # Gets the offer batch for sale first (qty > 0 and offer = 2)
    for product in products:
        product.discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()

        # original price
        product.original_price_batch = product.batches.filter(quantity__gt=0).first()

        product.dietary_categories_names = product.dietary_categories.values_list('name', flat=True)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product.objects.prefetch_related(
        'batches', 'dietary_categories'
    ), pk=product_id)

    # Gets the offer batch for sale first (qty > 0 and offer = 2)
    discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()
    original_price_batch = product.batches.filter(quantity__gt=0).first()

    # Gets dietaries categories for each products
    dietary_categories_names = product.dietary_categories.values_list('name', flat=True)

    context = {
        'product': product,
        'discount_price_batch': discount_price_batch,
        'original_price_batch': original_price_batch,
        'dietary_categories_names': dietary_categories_names,
    }

    return render(request, 'products/product_detail.html', context)
