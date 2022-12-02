from django.contrib import admin
from .models import Product
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    fields = ('title','content', 'price',)
    list_display = ('sale_price',)
    
    
admin.site.register(Product,AdminProduct)