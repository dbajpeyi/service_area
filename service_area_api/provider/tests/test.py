from rest_framework.test import APIRequestFactory
from provider.models import *
from django.test import TestCase


class ProviderAPITest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
	self.providers = Provider.objects.all()
	self.serviceareas = ServiceArea.objects.all()

    def test_details(self):
	
	print self.providers
	self.assertEqual(10,10)
