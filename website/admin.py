from django.contrib import admin
from .models import Product, ContactMessage, Cart, CartItem, Order, OrderItem

# 1. Product Admin
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


# 2. Contact Message Admin
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


# 3. Cart & CartItem Admin
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


# 4. Order & OrderItem Admin
admin.site.register(OrderItem)  # OrderItem simple register kar diya

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'id')