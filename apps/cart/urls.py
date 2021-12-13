from django.urls.conf import path


from .views import * 


urlpatterns = [
    path('', CartView.as_view()),
    path('add-to-cart/<slug:slug>/', AddToCartView.as_view()),
    path('remove-from-cart/<int:id>/', RemoveFromCartView.as_view()),
]
