from django.shortcuts import render, get_object_or_404
from django.db.models import Min, F, Q
from django.db.models.functions import Lower
from django.db import connection
from django.db.models import Min, FloatField
from django.db.models.functions import Cast
from django.contrib.auth.decorators import login_required
from products.models import Product, Batch, DietaryCategory, COOKING_PROCESS_CHOICES
from .forms import BatchForm


# Create your views here.

@login_required
def admin_panel(request):
    """ Displays all the shop managing options in a menu """
    
    if not request.user.is_superuser:
        return render(request, '403.html')
    
    return render(request, 'shop_admin/admin_panel.html')

@login_required
def manage_batches(request):
    """ View to display all batches ordered by batch.id with sorting and search """
    
    # Sorting Fields
    sortable_fields = ['product__short_widget_name', 'batch_number',
                       'expiry_date', 'quantity', 'offer', 
                       'discount_percentage', 'sale_price']

    sort_by = request.GET.get('sort_by', 'expiry_date')  # Default sort by 'id'
    sort_order = request.GET.get('sort_order', 'asc')

    if sort_by not in sortable_fields:
        sort_by = 'id'

    search_query = request.GET.get('q', '')

    batches = Batch.objects.all()

    if search_query:
        print(f"Search query: {search_query}")
        print(f"Batches before filter: {batches.count()}")
        batches = batches.filter(
            Q(batch_number__icontains=search_query) |
            Q(product__short_widget_name__icontains=search_query) |
            Q(expiry_date__icontains=search_query) |
            Q(sale_price__icontains=search_query) |
            Q(offer__icontains=search_query) |
            Q(quantity__icontains=search_query)
        )
        print(f"Batches after filter: {batches.count()}")

    if sort_order == 'desc':
        batches = batches.order_by(f'-{sort_by}')
    else:
        batches = batches.order_by(sort_by)

    context = {
        'batches': batches,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'search_query': search_query,
    }
    return render(request, 'shop_admin/manage_batches.html', context)

@login_required
def add_batch(request):
    """ Add a batch to an existing product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            batch = form.save()
            messages.success(request, 'Successfully added batch!')
            return redirect(reverse('batch_detail', args=[batch.id]))
        else:
            messages.error(request, 'Failed to add batch. Please ensure the form is valid.')
    else:
        form = BatchForm()

    context = {
        'form': form,
    }

    return render(request, 'shop_admin/add_batch.html', context)