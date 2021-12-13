from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}



