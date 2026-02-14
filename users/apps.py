from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Пользователи и профили'

    def ready(self):
        """
        Импортируем сигналы при запуске приложения
        БЕЗ ЭТОГО СИГНАЛЫ НЕ БУДУТ РАБОТАТЬ!
        """
        import users.signals  # noqa
