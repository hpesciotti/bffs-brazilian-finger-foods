from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='shop_admin'),
    path('add_batch/', views.add_batch, name='add_batch'),
    path('manage_batches/', views.manage_batches, name='manage_batches'),
    path('manage_products/', views.manage_products, name='manage_products'),
    path('best_seller/<int:product_id>/', views.best_seller, name='best_seller'),
    path('update_price/<int:product_id>/', views.update_price, name='update_price'),
    path('apply_discount/<int:batch_id>/', views.apply_discount, name='apply_discount'),
    path('edit_batch/<int:batch_id>/', views.edit_batch, name='edit_batch'),
    path('delete_batch/<int:batch_id>/', views.delete_batch, name='delete_batch'),
]