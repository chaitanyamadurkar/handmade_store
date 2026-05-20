from rest_framework import serializers
from .models import Order
from products.models import Product

class OrderSerializer(serializers.ModelSerializer):
    product_name  = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'customer_name', 'customer_email', 'customer_phone',
            'address', 'product', 'product_name', 'product_price',
            'quantity', 'total_price', 'status', 'notes', 'created_at',
        ]
        read_only_fields = ['total_price', 'status', 'created_at']

    def validate(self, data):
        product = data.get('product')
        quantity = data.get('quantity', 1)
        if product and product.stock < quantity:
            raise serializers.ValidationError(
                f'Only {product.stock} item(s) in stock.'
            )
        return data
