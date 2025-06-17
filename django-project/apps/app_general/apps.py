from django.apps import AppConfig


# make sure to update AppClassName and App name
class AppGeneralConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.app_general'
    verbose_name = 'Application general of the project'
    label = 'app_general'
