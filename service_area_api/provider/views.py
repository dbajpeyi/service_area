from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry



class ProviderViewSet(viewsets.ModelViewSet):

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ServiceAreaViewSet(viewsets.ModelViewSet):

    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()



class ServiceAreaByLatLng(ListAPIView):


    def get_queryset(self):
        lat = self.kwargs.get('lat')
        lng = self. kwargs.get('lng')
        pt =  GEOSGeometry('POINT ({0} {1})'.format(lng, lat), srid=4326) 
        print lat, lng , pt
        return ServiceArea.objects.filter(area__contains = pt)

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServiceAreaSerializer(queryset, many=True)
        return Response(serializer.data)
