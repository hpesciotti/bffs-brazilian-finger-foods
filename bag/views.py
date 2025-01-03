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
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Verifica se o item já está no carrinho
    if item_id in bag:
        # Verifica se o valor atual é um número (inteiro)
        if isinstance(bag[item_id], int):
            bag[item_id] += quantity
        else:
            # Caso o valor não seja um número, reinicializa o valor para a quantidade
            bag[item_id] = quantity
    else:
        # Adiciona um novo item ao carrinho
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    print(request.session['bag'])  # Para fins de depuração
    return redirect(redirect_url)



# def add_to_bag(request, item_id):
#     """ Add a quantity of the specified batch to the shopping cart """

#     # Use item_id para buscar o lote (batch)
#     product = get_object_or_404(Batch.objects.prefetch_related(
#         'products', 'dietary_categories'
#     ), pk=batch.product)
#     quantity = int(request.POST.get('quantity'))
#     redirect_url = request.POST.get('redirect_url')
#     bag = request.session.get('bag', {})  # Carrinho da sessão

#     # Se o item já estiver no carrinho, atualize a quantidade
#     if item_id in list(bag.keys()):
#         bag[item_id] += quantity
#         messages.success(
#             request,
#             f'Updated {product.name} quantity to {bag[item_id]["quantity"]}'
#         )
#     else:
#         # Adicione um novo item ao carrinho
#         bag[item_id] = quantity
#         messages.success(
#             request,
#             f'Added {product.name} to your cart'
#         )

#     # Atualize o carrinho na sessão
#     request.session['bag'] = bag
#     return redirect(redirect_url)

# def adjust_bag(request, batch_id):
#     """Adjust the quantity of the specified batch to the specified amount"""

#     batch = get_object_or_404(Batch, pk=batch_id)
#     product = batch.product
#     quantity = int(request.POST.get('quantity'))
#     bag = request.session.get('bag', {})

#     if quantity > 0:
#         if batch_id in bag:
#             bag[batch_id]['quantity'] = quantity
#             messages.success(
#                 request,
#                  f'Updated {product.name} quantity to {bag[batch_id]["quantity"]}'
#             )
#         else:
#             messages.error(request, "This item is not in your cart.")
#     else:
#         if batch_id in bag:
#             bag.pop(batch_id)
#             messages.success(
#                 request,
#                  f'Removed {product.name} (Batch {batch.batch_number}) from your cart'
#             )
#         else:
#             messages.error(request, "This item is not in your cart.")

#     request.session['bag'] = bag
#     return redirect(reverse('view_bag'))


# def remove_from_bag(request, batch_id):
#     """Remove the item from the shopping cart"""

#     try:
#         batch = get_object_or_404(Batch, pk=batch_id)
#         product = batch.product
#         bag = request.session.get('bag', {})

#         if batch_id in bag:
#             bag.pop(batch_id)
#             messages.success(
#                 request,
#                  f'Removed {product.name} from your cart'
#             )
#         else:
#             messages.error(request, "This item is not in your cart.")

#         request.session['bag'] = bag
#         return HttpResponse(status=200)

#     except Exception as e:
#         messages.error(request, f'Error removing item: {e}')
#         return HttpResponse(status=500)
