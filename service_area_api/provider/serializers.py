from rest_framework import serializers
from provider.models import Provider, ServiceArea

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider

class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
