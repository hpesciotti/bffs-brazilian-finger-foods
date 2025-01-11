from django.contrib import admin
from .models import Product, Batch, DietaryCategory


@admin.register(DietaryCategory)
class DietaryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_id", "short_widget_name",
                    "price", "best_seller")
    search_fields = ("name", "short_widget_name", "product_id")
    list_filter = ("dietary_categories__name",
                   "cooking_process", "best_seller")
    ordering = ("short_widget_name",)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("batch_number", "get_product_short_widget_name",
                    "expiry_date", "quantity", "offer",
                    "discount_percentage", "sale_price")
    search_fields = (
        "batch_number", "product__short_widget_name", "sale_price")
    list_filter = ("expiry_date", "offer", "sale_price")
    ordering = ("sale_price", )

    def get_product_short_widget_name(self, obj):
        return obj.product.short_widget_name
