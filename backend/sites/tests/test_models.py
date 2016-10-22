import pytest
from unittest.mock import patch
from datetime import datetime
from utils.fixtures import mongo

from ..models import Site


@pytest.mark.usefixtures('mongo')
class SiteTests:

    def test_object_creation(self):
        site = Site(name='test_site')
        site.save()
        assert Site.objects.first().name == site.name

    def test_modified_field_is_updated_on_document_save(self):
        site = Site(name='test_site')
        site.save()
        with patch('sites.models.timezone.now') as tznow_mock:
            tznow_mock.return_value = datetime(1999, 1, 1)
            site.name = 'after this save modified field should get updated with ^'
            site.save()
        assert site.modified == datetime(1999, 1, 1)

    @pytest.mark.skip("not implemented | works for save only")
    def test_modified_field_is_updated_on_query_update(self):
        site = Site(name='test_site')
        site.save()
        with patch('sites.models.timezone.now') as tznow_mock:
            tznow_mock.return_value = datetime(1999, 1, 1)
            Site.objects.all().update(name='set modified to ^')
        assert site.modified == datetime(1999, 1, 1)
