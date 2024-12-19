from django.shortcuts import render
from .models import Product, Batch

# Create your views here.

def all_products(request):
    """
    Returns all products and render main product page
    """
    return render(request, 'products/products.html')
