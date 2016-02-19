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
