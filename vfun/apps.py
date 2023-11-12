from django.apps import AppConfig


class VfunConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "vfun"

    def ready(self):
        import vfun.signals
