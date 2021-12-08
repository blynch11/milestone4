from django.contrib import admin
from. models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    
    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total',)  
    fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total','full_name', 'email', 'country', 'eircode', 
            'town_or_city', 'street_address1', 'street_address2',) 

    list_display = ('order_number', 'date', 'full_name', 'delivery_cost', 'order_total', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

# Register your models here.
