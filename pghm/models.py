#from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Webcam(models.Model):
	geom = models.PointField(blank=True, null=True)
	station = models.CharField(max_length=254, blank=True, null=True)
	site = models.CharField(max_length=254, blank=True, null=True)
	img = models.CharField(max_length=254, blank=True, null=True)
	nom = models.CharField(max_length=254, blank=True, null=True)
	#lat = models.FloatField(blank=True, null=True)
	#lon = models.FloatField(blank=True, null=True)
	yaw = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.station + ': ' + self.nom
		#return '{nom} {station}'.format(nom=self.nom, station=self.station)    

	class Meta:
		managed = False
		db_table = 'webcam'
		permissions = (
            		("view_webcam", "Can see webcams"),
        			)


class Unite(models.Model):
    code = models.CharField(max_length=16)
    nom = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    secours = models.CharField(max_length=64, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    dept = models.CharField(max_length=3, blank=True, null=True)
    zoom = models.IntegerField()

    def __str__(self):
    	return self.code + ' : ' + self.nom

    class Meta:
        managed = True
        db_table = 'unite'