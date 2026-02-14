from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    СИГНАЛ: Автоматически создает профиль при регистрации пользователя
    Срабатывает ПОСЛЕ сохранения пользователя (post_save)
    """
    if created:  # Только при СОЗДАНИИ нового пользователя!
        Profile.objects.create(
            user=instance,
            # Можно задать значения по умолчанию
            city='Не указан',
            address='Не указан',
            is_age_verified=False
        )
        print(f'✅ Автоматически создан профиль для {instance.username}')  # Для отладки

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    СИГНАЛ: Автоматически сохраняет профиль при сохранении пользователя
    """
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # Если профиля нет - создаем
        Profile.objects.create(user=instance)