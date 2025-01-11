from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Add order line to admin panel
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Add order to admin panel
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag')

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'phone_number', 'eircode', 'street_address1',
              'street_address2', 'delivery_cost', 'order_total',
              'grand_total', 'original_bag')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
