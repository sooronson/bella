from django.contrib import admin

from .models import OrderItem, Order


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class BasketAdmin(admin.ModelAdmin):
    inlines = (OrderItemInLine, )

