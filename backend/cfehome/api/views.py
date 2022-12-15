from rest_framework import generics, mixins

from .serializer import ProductSerializer
from .models import Product

class ProductsMixinView(generics.GenericAPIView):
    pass




class ProductsListView(generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
# class ProductDeleteView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer 
    
    
# class ProductUptadeView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def perform_update(self, serializer):
        