import pytest
from unittest.mock import patch
from datetime import datetime
from utils.fixtures import mongo

from ..models import Location


@pytest.mark.usefixtures('mongo')
class LocationTests:

    def test_object_creation(self):
        location = Location(name='test_location')
        location.save()
        assert Location.objects.first().name == location.name

    def test_modified_field_is_updated_on_document_save(self):
        location = Location(name='test_location')
        location.save()
        with patch('locations.models.timezone.now') as tznow_mock:
            tznow_mock.return_value = datetime(1999, 1, 1)
            location.name = 'after this save modified field should get updated with ^'
            location.save()
        assert location.modified == datetime(1999, 1, 1)

    @pytest.mark.skip("not implemented | works for save only")
    def test_modified_field_is_updated_on_query_update(self):
        location = Location(name='test_location')
        location.save()
        with patch('locations.models.timezone.now') as tznow_mock:
            tznow_mock.return_value = datetime(1999, 1, 1)
            Location.objects.all().update(name='set modified to ^')
        assert location.modified == datetime(1999, 1, 1)
