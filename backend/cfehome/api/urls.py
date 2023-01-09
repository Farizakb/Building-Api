from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import ProductDetailView, ProductsListView

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('products', ProductsListView.as_view(), name = 'home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name = 'product-detail'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    
    # path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
    # path('product/<int:pk>', ProductDetailView.as_view(), name = 'home'),
]
