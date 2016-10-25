import mongoengine as me
from django.db import models
from django.utils import timezone


class Category(me.EmbeddedDocument):
    name = me.StringField(max_length=20, required=True)
    description = me.StringField()


class Location(me.Document):
    ABANDONED = 'abandoned'
    INACTIVE = 'inactive'
    ACTIVE = 'active'
    location_status = (
        (ABANDONED, 'Abandoned'),
        (INACTIVE, 'Non-existent'),
        (ACTIVE, 'Active'),
    )

    name = me.StringField(max_length=500, required=True)
    categories = me.EmbeddedDocumentListField(Category)
    description = me.StringField()
    coordinates = me.GeoPointField()
    status = me.StringField(max_length=10, choices=location_status, default=ABANDONED)
    modified = me.DateTimeField(required=True, default=timezone.now)

    @property
    def created(self):
        return self.id.generation_time

    def __str__(self):
        return self.name

    @classmethod
    def update_modified(cls, sender, document, **kwargs):
        """ used as a pre_save signal """
        document.modified = timezone.now()
