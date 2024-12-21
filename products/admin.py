from django.contrib import admin
from .models import Product, Batch, DietaryCategory

# Register your models here.

@admin.register(DietaryCategory)
class DietaryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("friendly_name", "name", "price", "best_seller")
    search_fields = ("name", "friendly_name", "product_id")
    list_filter = ("dietary_categories__name",
        "cooking_process", "best_seller")
    ordering = ("friendly_name",)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("batch_number", "product",
        "expiry_date", "quantity", "offer", "discount_percentage")
    search_fields = ("batch_number", "product__name")
    list_filter = ("expiry_date", "offer")
    ordering = ("expiry_date",)
