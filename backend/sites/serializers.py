from rest_framework_mongoengine import serializers

from .models import Site


class SiteSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Site
        fields = ('id', 'name', 'description', 'status', 'coordinates', 'modified', 'created')
