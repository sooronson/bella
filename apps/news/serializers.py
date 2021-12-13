from rest_framework.serializers import ModelSerializer

from .models import News


class NewsSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'slug', 'description', 'image', 'created_at')



