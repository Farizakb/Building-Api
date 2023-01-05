from rest_framework import generics, mixins, permissions, authentication
from .authentication import TokenAuthentication
from .serializer import ProductSerializer
from .models import Product
from .mixin import StaffEditorPermissionMixin 




class ProductsListView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
# class ProductDeleteView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer 
    
    
# class ProductUptadeView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def perform_update(self, serializer):
        