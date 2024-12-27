from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """ 
    A view to return the index page 
    """

    best_seller_products = Product.objects.filter(best_seller=True)

    context = {
        'best_seller_products': best_seller_products,
    }

    return render(request, 'home/index.html', context)