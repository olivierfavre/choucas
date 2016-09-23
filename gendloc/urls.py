from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^envoi', views.envoi_sms, name='envoi'),
    url(r'^maj/', views.maj, name='maj'),
    url(r'^geoloc/', views.geoloc, name='geoloc'),
]