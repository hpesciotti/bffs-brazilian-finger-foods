from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db.models import Min
from django.db.models.functions import Lower
from django.db import connection
from .models import Product, Batch, DietaryCategory, COOKING_PROCESS_CHOICES

# Create your views here.

from django.db.models import Min, F, Q

def all_products(request):
    """
    Returns all products and render main product page with filtering options.
    """
    search_term = request.GET.get('q', '').lower()
    dietary_category_filter = request.GET.get('dietary_category', '').lower()
    cooking_process_filter = request.GET.get('cooking_process', '').lower()
    offer_filter = request.GET.get('offer', None)
    sort_direction = request.GET.get('sort', 'asc')
    sort_key = request.GET.get('sort_by', 'name')

    # Prefetching related batches and dietary categories to avoid repeated queries
    products = Product.objects.prefetch_related('batches', 'dietary_categories')

    # Filters
    if search_term:
        products = products.filter(
            Q(name__icontains=search_term) |
            Q(full_name__icontains=search_term) |
            Q(short_widget_name__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(ingredients__icontains=search_term) |
            Q(dietary_categories__name__icontains=search_term)
        )

    if dietary_category_filter:
        products = products.filter(
            dietary_categories__name__icontains=dietary_category_filter
        )

    if cooking_process_filter:
        COOKING_PROCESS_MAP = {
            'baking': 1,
            'frying': 2,
            'frying or baking': 3,
        }
        cooking_process_value = COOKING_PROCESS_MAP.get(cooking_process_filter)
        if cooking_process_value:
            products = products.filter(cooking_process=cooking_process_value)

    if offer_filter:
        products = products.filter(batches__offer=offer_filter)

    # Annotate each product with the minimum sale_price from its related batches
    # Filter batches to only include those with quantity > 0 and a valid sale_price
    products = products.annotate(min_price=Min('batches__sale_price'))

    # Verificar se o cálculo está correto, talvez filtrando lotes inválidos
    products = products.filter(
        batches__quantity__gt=0,  # Garantir que os lotes têm quantidade
        batches__sale_price__isnull=False  # Garantir que o sale_price não seja nulo
    )

    # Ordering the products based on the selected criteria
    if sort_key == 'min_price':
        if sort_direction == 'asc':
            products = products.order_by('min_price')
        else:
            products = products.order_by('-min_price')
    elif sort_key == 'name':
        if sort_direction == 'asc':
            products = products.order_by('name')
        else:
            products = products.order_by('-name')

    # Set current sorting for use in the template
    current_sorting = f"{sort_key}_{sort_direction}"

    # Process each product to get discount and original prices
    for product in products:
        # Apply the price logic here (discount and original prices)
        discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()
        if discount_price_batch:
            product.discount_price_batch = discount_price_batch.sale_price
        else:
            product.discount_price_batch = None

        original_price_batch = product.batches.filter(quantity__gt=0).first()
        if original_price_batch:
            product.original_price_batch = original_price_batch.sale_price
        else:
            product.original_price_batch = None

        # Get dietary categories names
        product.dietary_categories_names = product.dietary_categories.values_list('name', flat=True)

    # Prepare context for rendering
    context = {
        'products': products,
        'cooking_process_choices': COOKING_PROCESS_CHOICES,
        'dietary_categories': DietaryCategory.objects.all(),
        'current_sorting': current_sorting,
    }

    # Debugging - Output the SQL query
    for product in products:
        print(f"Product: {product.name}, Min Price: {product.min_price}")
        print(f"SQL Query: {connection.queries[-1]['sql']}")

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product.objects.prefetch_related(
        'batches', 'dietary_categories'
    ), pk=product_id)

    # Gets the offer batch for sale first (qty > 0 and offer = 2)
    discount_price_batch = product.batches.filter(quantity__gt=0, offer=2).first()
    if discount_price_batch:
        discount_price_batch = discount_price_batch.sale_price  # Use the calculated sale_price
    else:
        discount_price_batch = None

    # Gets the original price batch (qty > 0)
    original_price_batch = product.batches.filter(quantity__gt=0).first()
    if original_price_batch:
        original_price_batch = original_price_batch.sale_price  # Use the calculated sale_price
    else:
        original_price_batch = None


    # Gets dietary categories names
    dietary_categories_names = product.dietary_categories.values_list('name', flat=True)

    print(f"Discount Price: {discount_price_batch}, Original Price: {original_price_batch}")

    if not product.batches.exists():
        print("No batches found for this product")

    context = {
        'product': product,
        'discount_price_batch': discount_price_batch,
        'original_price_batch': original_price_batch,
        'dietary_categories_names': dietary_categories_names,
    }

    return render(request, 'products/product_detail.html', context)
