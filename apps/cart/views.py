from rest_framework import response, status, generics, permissions, views
from rest_framework.exceptions import NotAcceptable
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models  import CartProduct, Cart 
from .serializers import CartSerializer, CartProductSerializer
from  apps.product.models import Product






class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes =(permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        serializer = CartSerializer(cart)
        return response.Response(serializer.data)



class AddToCartView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def update(self, request, *args, **kwargs):
        quantity = int(request.data.get("quantity"))
        slug = kwargs.get('slug')
        user = request.user
        product = get_object_or_404(Product, slug=slug)
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_product = CartProduct.objects.filter(
            product=product, cart=cart
            )

        if cart_product:
            raise NotAcceptable(
                'You already have this product in your cart'
                )

        if quantity > product.quantity:
            raise NotAcceptable(
                "Not enough product in stock!!! We'll restock it ASAP"
                )
        cart_product = CartProduct.objects.get_or_create(
            product=product, quantity=quantity, cart=cart
            )
        total_price = product.price * quantity
        cart.total_price += total_price
        cart.save()
        return response.Response(
            {'message': 'You successfuly added product into your cart'},
            status=status.HTTP_201_CREATED
            )



class RemoveFromCartView(generics.UpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        cart = Cart.objects.get(user=request.user)
        product = CartProduct.objects.get(cart=cart, id=id)
        product.delete()
        cart.total_price -= product.total_price
        cart.save()
        return response.Response(
            {'detail':"Successfully deleted!!!"},
            status=status.HTTP_204_NO_CONTENT
            )

