from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('phone',)}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'is_age_verified', 'created_at')
    list_filter = ('city', 'is_age_verified', 'created_at')
    search_fields = ('user__username', 'user__email', 'address')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Пользователь', {
            'fields': ('user',)
        }),
        ('Личная информация', {
            'fields': ('avatar', 'birth_date', 'is_age_verified', 'age_verified_at')
        }),
        ('Адрес доставки', {
            'fields': ('city', 'address', 'postal_code')
        }),
        ('Настройки', {
            'fields': ('email_notifications', 'sms_notifications')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        }),
    )