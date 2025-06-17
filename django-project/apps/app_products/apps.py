from django.apps import AppConfig


# make sure to update AppClassName and App name
class AppProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.app_products'
    verbose_name = 'Application for products'
    label = 'app_products'
