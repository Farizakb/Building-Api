from django.urls import path
from .views import ProductDetailView, ProductsListView

urlpatterns = [
    path('products', ProductsListView.as_view(), name = 'home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
]
