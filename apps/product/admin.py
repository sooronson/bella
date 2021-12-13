from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class AdditionalInline(admin.TabularInline):
    model = Additional
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    inlines = [ImageInline, AdditionalInline]


admin.site.register(Image)
admin.site.register(Favorite)
admin.site.register(Color)