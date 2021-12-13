from rest_framework import serializers

from .models import *
from apps.accounts.serializers import RegisterSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ('title', 'parent', 'slug',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.child.exists():
            representation['child'] = CategorySerializer(
                instance=instance.child.all(), many=True).data
        return representation


class ImageSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.title')

    class Meta:

        model = Image
        fields = ('product', 'image')


class ProductSerializer(serializers.ModelSerializer):

    color = serializers.CharField(source='color.title')
    category = serializers.CharField(source='category.title')

    class Meta:

        model = Product
        fields = (
            'category',
            'title', 
            'slug',
            'description',
            'quantity', 
            'article', 
            'size',
            'color',
            'get_final_price',
            'is_favorite',
            )


class ProductDetailSerializer(serializers.ModelSerializer):

    color = serializers.CharField(source='color.title')
    category = serializers.CharField(source='category.title')
    product_image = ImageSerializer(many=True)

    class Meta:

        model = Product
        fields = (
            'category',
            'title', 
            'description',
            'article', 
            'size',
            'color',
            'get_final_price',
            'is_favorite',
            'product_image'
            )


class ColorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Color
        fields = ('color', 'title',)


class FavoriteSerializer(serializers.ModelSerializer):

    product = ProductDetailSerializer(many=True)
    user = serializers.CharField(source='user.first_name')

    class Meta:
        
        model = Favorite
        fields = ('user', 'product',)


class AdditionalSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    user = RegisterSerializer()

    class Meta:

        model = Additional
        fields = ('key', 'value', 'product')
