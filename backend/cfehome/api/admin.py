from django.contrib import admin
from .models import Product
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    fields = ('user','title','content', 'price',)
    list_display = ('title',)
    
    
    
admin.site.register(Product,AdminProduct)