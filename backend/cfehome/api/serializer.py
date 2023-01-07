from rest_framework import serializers
from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk')
    title = serializers.CharField(validators=[validators.validate_title])
    
    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price'
        ]
        
        