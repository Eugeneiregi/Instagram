from django.apps import AppConfig
from .signals


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
