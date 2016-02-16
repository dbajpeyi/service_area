from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ProviderListView(ListAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()



