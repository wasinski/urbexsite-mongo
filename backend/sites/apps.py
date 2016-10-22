from django.apps import AppConfig
from mongoengine.signals import pre_save


class SitesConfig(AppConfig):
    name = 'sites'

    def ready(self):
        from .models import Site
        pre_save.connect(receiver=Site.update_modified, sender=Site)
