from django.contrib import admin
from .models import Product, Batch, DietaryCategory, Allergens

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_process')
    list_filter = ('cooking_process', 'dietary_categories', 'allergens')
    search_fields = ('name', 'description', 'dietary_info')
    filter_horizontal = ('dietary_categories', 'allergens')
    ordering = ('name',)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('product', 'batch_number', 'expiry_date', 'quantity', 'offer',
     'discount_percentage')
    list_filter = ('expiry_date', 'offer')
    search_fields = ('batch_number', 'product__name')
    ordering = ('expiry_date',)
    date_hierarchy = 'expiry_date'


@admin.register(DietaryCategory)
class DietaryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Allergens)
class AllergensAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)
