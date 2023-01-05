from rest_framework import viewsets

from .models import Product
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial UPdate
    delete -> destroy 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default