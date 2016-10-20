import mongoengine as me
from random import random

from ..models import Site


class SiteTests:

    def setup_method(self):
        self.db = me.connect('mongoenginetest', host='mongodb://localhost')

    def teardown_method(self):
        self.db.drop_database('mongoenginetest')
        self.db.close()

    def test_object_creation(self):
        site = Site(name='test_site')
        site.save()
        assert Site.objects.first().name == site.name
