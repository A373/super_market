from django.contrib import admin
from .models import Product, Transaction


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'selling_price', 'buying_price', 'inventory', 'mrp']
    search_fields = ['product_name']


admin.site.register(Product, ProductAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'mobile_number', 'product_list']
    search_fields = ['customer_name']


admin.site.register(Transaction, TransactionAdmin)
