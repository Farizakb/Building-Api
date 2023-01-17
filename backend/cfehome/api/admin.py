from django.contrib import admin
from .models import Product
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    fields = ('user','title','content', 'price',)
    list_display = ('title','content','user','price','public', 'photo')
    list_editable = ('content','user','price','public', 'photo')
    
    
    
admin.site.register(Product,AdminProduct)