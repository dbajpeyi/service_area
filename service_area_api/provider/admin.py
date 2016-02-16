from django.contrib import admin
from django.contrib.gis import admin

from provider.models import *
# Register your models here.

class ProviderAdmin(admin.ModelAdmin):
    pass

class ServiceAreaAdmin(admin.GeoModelAdmin):
    pass

class CurrencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Provider, ProviderAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
admin.site.register(Currency, CurrencyAdmin)

