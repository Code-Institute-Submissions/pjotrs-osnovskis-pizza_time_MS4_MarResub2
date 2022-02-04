from django.contrib import admin
from .models import Category, Product, Pizza, Topping


class ProductAdmin(admin.ModelAdmin):
    """
    Admin customization for Products section to show relevan information
    for users convenience.
    """
    list_display = (
        'pizza',
        'category',
        'total_price',
    )

    ordering = ('pizza',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Pizza)
admin.site.register(Topping)
