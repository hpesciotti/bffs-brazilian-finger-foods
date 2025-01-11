from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='shop_admin'),
    path('add_batch/', views.add_batch, name='add_batch'),
    path('manage_batches/', views.manage_batches, name='manage_batches'),
    path('apply_discount/<int:batch_id>/', views.apply_discount, name='apply_discount'),
    path('edit_batch/<int:batch_id>/', views.edit_batch, name='edit_batch'),
    path('delete_batch/<int:batch_id>/', views.delete_batch, name='delete_batch'),
]