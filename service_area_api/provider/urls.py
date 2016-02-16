from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'providers', views.ProviderViewSet)
router.register(r'area', views.ServiceAreaViewSet)
urlpatterns = router.urls

urlpatterns.extend([
    url(r'^area/(?P<lng>\-?\d+\.\d+)/(?P<lat>\-?\d+\.\d+)/$', views.ServiceAreaByLatLng.as_view()),
])


