from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Batch, DietaryCategory, COOKING_PROCESS_CHOICES

# Create your views here.

def all_products(request):
    """
    Returns all products and render main product page with filtering options.
    """
    # Get query parameters
    search_term = request.GET.get('q', '').lower()
    dietary_category_filter = request.GET.get('dietary_category', '').lower()
    cooking_process_filter = request.GET.get('cooking_process', '').lower()
    sort_direction = request.GET.get('sort', 'asc')  # Default to ascending
    sort_option = request.GET.get('sort_by', 'name')  # Default to sorting by 'name'

    # Fetch products
    products = Product.objects.prefetch_related('batches', 'dietary_categories')

    # Apply filters
    if search_term:
        products = products.filter(
            Q(name__icontains=search_term) |
            Q(full_name__icontains=search_term) |
            Q(short_widget_name__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(ingredients__icontains=search_term)
        )

    if dietary_category_filter:
        products = products.filter(
            dietary_categories__name__icontains=dietary_category_filter
        )

    if cooking_process_filter:
        products = products.filter(
            cooking_process__iexact=cooking_process_filter
        )

    # Apply sorting logic
    if sort_option == 'price_asc':
        products = products.order_by('sale_price')
    elif sort_option == 'price_desc':
        products = products.order_by('-sale_price')
    elif sort_option == 'name_asc':
        products = products.order_by('name')
    elif sort_option == 'name_desc':
        products = products.order_by('-name')
    elif sort_option == 'category_asc':
        products = products.order_by('dietary_categories__name')
    elif sort_option == 'category_desc':
        products = products.order_by('-dietary_categories__name')

    # Prepare products with additional data
    for product in products:
        product.discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()
        product.original_price_batch = product.batches.filter(quantity__gt=0).first()
        product.dietary_categories_names = product.dietary_categories.values_list('name', flat=True)

    context = {
        'products': products,
        'cooking_process_choices': COOKING_PROCESS_CHOICES,
        'dietary_categories': DietaryCategory.objects.all(),
        'current_sorting': sort_option
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
