from django.contrib import admin
from .models import Product, ContactMessage

from .models import (
    Product,
    ContactMessage,
    Cart,
    CartItem,
)
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "featured",
        "available",
    )

    list_filter = (
        "featured",
        "available",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "created_at",
    )

    ordering = (
        "-created_at",
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "cart",
        "product",
        "quantity",
        "total_price",
    )

    list_filter = (
        "cart",
    )

    search_fields = (
        "product__name",
    )

# Register your models here.
