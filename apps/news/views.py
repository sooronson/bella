from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import NewsSerializer
from .models import News
from .paginations import StandardResultSetPagination


class NewsListApiView(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = StandardResultSetPagination
    lookup_field = 'slug'

