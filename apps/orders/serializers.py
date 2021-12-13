from rest_framework import serializers

from .models import Order, OrderItem
from apps.product.models import Product, Image
from apps.product.serializers import (
    ColorSerializer
)


class OrderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class ProductOrderSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    product_image = OrderImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'title', 'article', 'color',
            'size', 'price', 'get_final_price', 'product_image'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductOrderSerializer()

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')


class OrdersListSerializer(serializers.ModelSerializer):
    fnl_total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'create_at',
            'fnl_total_price',
            'status',
        )


class OrderDetailSerializer(serializers.ModelSerializer):
    order_products = OrderItemSerializer(read_only=True, many=True)
    fnl_total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'address', 'create_at',
                  'order_products',
                  'status',
                  'fnl_total_price')
