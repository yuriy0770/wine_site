from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50, verbose_name='')

    def __str__(self):
        return self.phone


class Profile(models.Model):
    """Профиль пользователя - расширенная информация"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile',   verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True,null=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес доставки', blank=True, null=True)
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс', blank=True, null=True)
    is_age_verified = models.BooleanField(default=False, verbose_name='Возраст подтвержден')
    age_verified_at = models.DateTimeField(verbose_name='Дата подтверждения возраста',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания профиля')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Дата обновления')
    email_notifications = models.BooleanField(default=True, verbose_name='Email-уведомления')
    sms_notifications = models.BooleanField(default=False, verbose_name='SMS-уведомления')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-created_at']

    def __str__(self):
        return f'Профиль {self.user.username}'

    @property
    def full_name(self):
        """Полное имя пользователя"""
        return f'{self.user.first_name} {self.user.last_name}'.strip() or self.user.username

    @property
    def is_adult(self):
        """Проверка совершеннолетия (18+)"""
        if not self.birth_date:
            return False
        from datetime import date
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age >= 18