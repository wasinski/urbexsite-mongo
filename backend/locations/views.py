from rest_framework_mongoengine.viewsets import ModelViewSet

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
