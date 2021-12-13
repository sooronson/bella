from django.contrib import admin

from .models import About, AboutDescription, Image, Contact


class ImagesTabularInline(admin.TabularInline):
    model = Image
    fields = ('image',)
    extra = 1


class AboutDescriptionInline(admin.TabularInline):
    model = AboutDescription
    fields = ('description',)
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = (ImagesTabularInline, AboutDescriptionInline)
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone_number', 'email',
        'address', 'ok', 'instagram',
        'facebook', 'vk'
    )
    list_display_links = ('id', 'phone_number')
