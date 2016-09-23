"""djmapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib.gis import admin
from pghm import views as pghm_views
from django.contrib.auth import views as auth_views
from pghm.models import Webcam, Unite
#from django.views.generic import TemplateView
#from djgeojson.views import GeoJSONLayerView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gendloc/', include('gendloc.urls')),
    url(r'^$', pghm_views.home, name='home'),
    url(r'^camera.geojson$', pghm_views.MapLayer.as_view(model=Webcam, properties=('nom','img','site',)), name='camera'),
    #url(r'^webcams/', TemplateView.as_view(template_name='pghm/wcams.html'), name='wcams'),
    #url(r'^webcams.geojson/', GeoJSONLayerView.as_view(model=Webcam), name='wcamsdata'),
    #url(r'^webcamdata$', views.wcamdata, name='webcams'),
    #url(r'^cams.data/', views.cam_view, name='camser'),
    #url(r'^ski.data/', ski_view, name='skiser'),
    #url(r'^zone.data/', zone_view, name='zoneser'),
    #url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^logout/$', auth_views.logout_then_login),
    url('^', include('django.contrib.auth.urls')),
]