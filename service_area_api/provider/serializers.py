from rest_framework import serializers
from provider.models import Provider, ServiceArea
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider

class ServiceAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        geo_field = 'area'


    def create(self, validated_data):
        try:
            return ServiceArea.objects.create(**validated_data)
        except TypeError:
            error = {'area' : 'Can only accept GeoJson type Polygon'}
            raise serializers.ValidationError(error)

