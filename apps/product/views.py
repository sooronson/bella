from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import generics, response, permissions, status, filters
from rest_framework.exceptions import NotAcceptable, ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


from .serializers import (
    ProductDetailSerializer, 
    CategorySerializer, FavoriteSerializer)
from .models import (
    Product, Category, Favorite, 
) 


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CategoryAPIView(generics.RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductAPIView(generics.RetrieveAPIView):

    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    permissions_classes = (permissions.IsAuthenticated,)

class ProductApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    pagination_class = StandardPagination
    filterset_fields = ('title', 'price', 'category')

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(category__icontains=search) | 
                Q(description__icontains=search))
        return queryset


class AddToFavoriteView(generics.UpdateAPIView):

    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def update(self, request, *args, **kwargs):
        user = request.user
        favorites, _ = Favorite.objects.get_or_create(user=user)
        slug = kwargs.get('slug')
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise NotAcceptable("No product in stock with such a name")
        if Favorite.objects.filter(product=product).exists():
            raise ValidationError("This product is already in")
        favorites.product.add(product)
        product.is_favorite = True
        product.save()
        serializer = FavoriteSerializer(favorites)
        return response.Response(
            serializer.data, status=status.HTTP_202_ACCEPTED
            )


class RemoveFromFavoritesView(generics.UpdateAPIView):

    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def update(self, request, *args, **kwargs):
        user = request.user
        slug = kwargs.get('slug')
        favorites = Favorite.objects.get(user=user)
        product = Product.objects.get(slug=slug)
        if Favorite.objects.filter(product=product).exists():
            favorites.product.remove(product)
            product.is_favorite = False
        return response.Response({
            'detail': f"{product.title} successfully removed from favorites"},
            status=status.HTTP_204_NO_CONTENT)




class FavoritesView(generics.RetrieveAPIView):

    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_object(self):
        return get_object_or_404(Favorite, user=self.request.user)




