from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('apps.accounts.urls')),
    path('news/', include('apps.news.urls')),
    path('info/', include('apps.info.urls')),
    path('product/', include('apps.product.urls')),
    path('orders/', include('apps.orders.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
