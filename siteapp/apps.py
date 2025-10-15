from django.apps import AppConfig

class SiteappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteapp'   # << must be exactly the package name, all lowercase
