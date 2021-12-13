from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    list_display = ('id', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_display_links = ('id', 'phone_number', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name', 'is_active')
    ordering = ('phone_number',)



