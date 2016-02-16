from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets

class ProviderViewSet(viewsets.ModelViewSet):

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()



