import mongoengine as me
import pytest
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Site
from ..factories import SiteFactory, CategoryFactory


client = APIClient()


class SiteViewSetTests:

    def setup_method(self):
        self.db = me.connect('mongoenginetest', host='mongodb://localhost')

    def teardown_method(self):
        self.db.drop_database('mongoenginetest')
        self.db.close()

    def test_list_view_on_empty_collection(self):
        """ no data was created """
        response = client.get('/sites/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == []
