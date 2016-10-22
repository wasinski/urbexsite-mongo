import pytest
from utils.fixtures import mongomock

from ..models import Site


@pytest.mark.usefixtures('mongomock')
class SiteTests:

    def test_object_creation(self):
        site = Site(name='test_site')
        site.save()
        assert Site.objects.first().name == site.name
