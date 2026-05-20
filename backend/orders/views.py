from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    """POST /api/orders/ — place a new order"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        # Reduce stock
        product = order.product
        product.stock -= order.quantity
        product.save()
