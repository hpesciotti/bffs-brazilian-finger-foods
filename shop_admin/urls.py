from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='shop_admin'),
    path('add_batch/', views.add_batch, name='add_batch'),
]