from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductListView(generics.ListAPIView):
    """GET /api/products/ — list all products. Filter by ?category=id or ?featured=true"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.select_related('category').all()
        category = self.request.query_params.get('category')
        featured = self.request.query_params.get('featured')
        if category:
            qs = qs.filter(category__slug=category)
        if featured == 'true':
            qs = qs.filter(is_featured=True)
        return qs


class ProductDetailView(generics.RetrieveAPIView):
    """GET /api/products/<id>/"""
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer


class CategoryListView(generics.ListAPIView):
    """GET /api/products/categories/"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
