import mongoengine as me
import pytest
from rest_framework import status
from rest_framework.test import APIClient

from utils.fixtures import mongo
from ..models import Site
from ..factories import SiteFactory, CategoryFactory


client = APIClient()


@pytest.mark.usefixtures('mongo')
class SiteViewSetTests:

    def test_list_view_on_empty_collection(self):
        """ no data was created """
        response = client.get('/sites/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == []

    def test_list_view_with_2_objects_created(self):
        SiteFactory.create_batch(2)
        response = client.get('/sites/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
