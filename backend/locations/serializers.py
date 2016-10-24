from rest_framework_mongoengine import serializers

from .models import Location


class LocationSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'status', 'coordinates', 'modified', 'created')
