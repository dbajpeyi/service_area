from rest_framework.test import APIRequestFactory
from provider.models import *
from provider.views import *
from django.test import TestCase
from django.contrib.gis.geos import Polygon
from decimal import Decimal

class ProviderAPITest(TestCase):

    def _make_provider(self):
        self.currency = Currency.objects.create(name="US Dollar", code="USD", html_code="USD")
        self.provider = Provider.objects.create(
                name = "Test Provider", 
                email="dbajpeyi@gmail.com", 
                phone="9742803424", 
                language='af',
                currency=self.currency)

    def _make_service_area(self):
        poly = Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)))
        self.service_area = ServiceArea.objects.create(
                name = "Test Area",
                area = poly,
                price = Decimal(123.22),
                provider = self.provider,
        )

    def setUp(self):
        self.factory = APIRequestFactory()
	self.providers = Provider.objects.all()
	self.serviceareas = ServiceArea.objects.all()
        self._make_provider()
        self._make_service_area()

    def test_service_areas_when_points_is_inside_polygon(self):
        req = self.factory.get('/areas/26.0/26.0')	
        view = ServiceAreaByLatLng.as_view()
        resp = view(req, lat='26.0', lng='26.0')
        self.assertEqual(len(resp.data), 1)

    def test_no_service_areas_when_point_outside_polygons(self):
        req = self.factory.get('/areas/-7.0/36.0')	
        view = ServiceAreaByLatLng.as_view()
        resp = view(req, lat='-7.0', lng='36.0')
        self.assertEqual(len(resp.data), 0)




