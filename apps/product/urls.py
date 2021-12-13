from django.urls.conf import path


from .views import (
    ProductAPIView, AddToFavoriteView, RemoveFromFavoritesView, 
    FavoritesView, CategoryAPIView
) 


urlpatterns = [
    path('', ProductAPIView.as_view(), name = 'product'),
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('category/', CategoryAPIView.as_view(), name= 'product_category'),
    path('<slug:slug>/', ProductAPIView.as_view()),
    path('add-to-favorites/<slug:slug>/', 
        AddToFavoriteView.as_view(), name='add-to-favorites'),
    path('remove-from-favorites/<slug:slug>/', 
        RemoveFromFavoritesView.as_view(), name='remove_from-favorites')
]
