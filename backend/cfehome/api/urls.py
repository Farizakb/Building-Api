from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProductDetailView, ProductsListView

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('products', ProductsListView.as_view(), name = 'home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name = 'product-detail'),
    
    # path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
    # path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
]
