from django.urls import path

from .views import OrderView, OrderListView

urlpatterns = [
    path('my_orders/', OrderView.as_view({'get': 'list'})),
    path('my_orders/<int:id>/', OrderListView.as_view()),
]
