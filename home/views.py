from django.shortcuts import render
from products.models import Product, Batch

# Create your views here.

def index(request):
    """ 
    A view to return the index page 
    """

    best_seller_products = Product.objects.filter(best_seller=True)
    offer_products = Product.objects.filter(batch__offer=2)

    context = {
        'best_seller_products': best_seller_products,
        'offer_products':  offer_products,
    }

    return render(request, 'home/index.html', context)