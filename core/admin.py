from django.contrib import admin

from core.models import Item, Order, OrderItem

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)
    list_filter = ("title", "price",)
    search_fields = ("title", "price",)

admin.site.register(Item, ItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "start_date", "ordered",)
    list_filter = ("user", "start_date", "ordered",)
    search_fields = ("user", "start_date", "ordered",)

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("item",)
    list_filter = ("item",)
    search_fields = ("item",)

admin.site.register(OrderItem, OrderItemAdmin)