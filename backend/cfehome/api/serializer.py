from rest_framework import serializers
from .models import Product
from . import validators
from django.conf import settings


User = settings.AUTH_USER_MODEL
        
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
        
        
class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field = 'pk')
    title = serializers.CharField(validators=[validators.validate_title])
    
    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public'
        ]