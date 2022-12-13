from rest_framework import filters, generics

from shop.models import Product
from shop.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'sku']

    def get_queryset(self):
        queryset = Product.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = Product.objects.filter(status=status)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
