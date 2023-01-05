from rest_framework.routers import DefaultRouter

from api.viewset import ProductViewSet


router = DefaultRouter()


router.register('product-abc', ProductViewSet, basename='products')


urlpatterns = router.urls