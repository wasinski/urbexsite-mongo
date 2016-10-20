from rest_framework_mongoengine.viewsets import ModelViewSet

from .models import Site
from .serializers import SiteSerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
