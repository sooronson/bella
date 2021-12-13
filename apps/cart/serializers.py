from rest_framework import serializers

from .models import *


class CartProductSerializer(serializers.ModelSerializer):

    product = serializers.CharField(source='product.title')
    
    class Meta:    
        model = CartProduct
        fields = ('id', 'quantity', 'product',)


class CartSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='user.first_name', read_only=True)
    cart_products = CartProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = ('user', 'total_price', 'cart_products')
