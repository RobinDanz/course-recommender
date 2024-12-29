from django.apps import AppConfig
from django.db.backends.signals import connection_created


class FuzzyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fuzzy'

    def ready(self):
        connection_created.connect(init_fuzzy_system)


def init_fuzzy_system(sender, **kwargs):
    from fuzzy.logic import fuzzy_controller
    fuzzy_controller.FuzzyController()
