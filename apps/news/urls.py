from django.urls import path

from .views import NewsListApiView

urlpatterns = [
    path('news/', NewsListApiView.as_view({'get': 'list'})),
    path('news/<str:slug>/', NewsListApiView.as_view({'get': 'retrieve'})),

]
