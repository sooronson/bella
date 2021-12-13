from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


from .models import Order
from .permissions import IsOwnerOrReadOnly
from .serializers import OrderDetailSerializer, OrdersListSerializer
from .paginations import StandardResultsSetPagination


class OrderView(ModelViewSet):
    serializer_class = OrdersListSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'
    pagination_class = StandardResultsSetPagination


class OrderListView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        user_orders = Order.objects.filter(user=user)
        return user_orders
