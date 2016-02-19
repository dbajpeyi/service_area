from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
import uuid



class Provider(models.Model):
    """
    Model for providers; shuttle company owners
    """

    ext_id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=20)
    language=models.CharField(max_length=3, choices=settings.LANGUAGES) 
    currency = models.ForeignKey('Currency')


class Currency(models.Model):
    """
    Currency model, can store html code for rendering 
    currency symbols to html
    """

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    html_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class ServiceArea(models.Model):
    """
    Container model to contain polygons along with additional 
    fields like name and price provided in that area. Polygons
    are used to define areas on a globe. Each provider can create
    multiple polygons as their service areas along with the price
    they offer in those areas
    """
    
    ext_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    area = models.PolygonField()
    price= models.DecimalField(max_digits=5, decimal_places=2)
    provider=models.ForeignKey('Provider')

    def __unicode__(self):
        return self.name

