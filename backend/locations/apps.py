from django.apps import AppConfig
from mongoengine.signals import pre_save


class LocationsConfig(AppConfig):
    name = 'locations'

    def ready(self):
        from .models import Location
        pre_save.connect(receiver=Location.update_modified, sender=Location)
