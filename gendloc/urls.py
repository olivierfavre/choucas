from django.conf import settings
from django.conf.urls import include, patterns, url
#from django.contrib.gis import admin
from . import views
from .views import SmsList
from .views import SmsLoc
from gendloc import views as gendloc_views
from gendloc.models import Geoloc

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^envoi/$', views.envoi_sms, name='envoi'),
    url(r'^maj/$', SmsLoc.as_view(), name='smsloc_list'),
    url(r'^maj2/$', views.maj, name='sms2_list'),
    url(r'^maj3/$', SmsList.as_view(), name='sms_list'),  
    url(r'^geoloc/', views.geoloc, name='geoloc'),
    url(r'^loc.geojson$', gendloc_views.MapLayer.as_view(model=Geoloc, properties=('dt_geoloc','origine','precision','ua',)), name='loc'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]