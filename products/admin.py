from django.contrib import admin
from .models import Category, Product, Topping, Size

class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
    )
    exclude = (
        'name',
    )


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Topping, ToppingAdmin)
