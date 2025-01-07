from django.shortcuts import render
from products.models import Product, Batch

# Create your views here.

def index(request):
    """ 
    A view to return the index page 
    """

    best_seller_products =  Product.objects.prefetch_related(
        'batches', 'dietary_categories'
    ).filter(best_seller=True)

    offer_products = Product.objects.prefetch_related(
        "batches"
    ).filter(batches__offer=2)

    # Gets the offer batch for sale first (qty > 0 and offer = 2)
    for product in offer_products:
        product.discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()

        # original price
        product.original_price_batch = product.batches.filter(quantity__gt=0).first()

        product.dietary_categories_names = product.dietary_categories.values_list('name', flat=True)

    for product in best_seller_products:
        product.discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()

        # original price
        product.original_price_batch = product.batches.filter(quantity__gt=0).first()

        product.dietary_categories_names = product.dietary_categories.values_list('name', flat=True)


    context = {
        'best_seller_products': best_seller_products,
        'offer_products':  offer_products,
    }

    return render(request, 'home/index.html', context)

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request, exception=None):
    return render(request, '500.html', status=500)

def contacts(request):
    """Contatcs view with static information"""
    return render(request, 'home/contacts.html')