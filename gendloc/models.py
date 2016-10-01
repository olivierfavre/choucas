from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Sms(models.Model):
    dt_envoi = models.DateTimeField(auto_now_add=True)
    dt_reception = models.DateTimeField(blank=True, null=True)
    dt_statut = models.DateTimeField(blank=True, null=True)
    unite = models.CharField(max_length=64, blank=True, null=True)
    utilisateur = models.CharField(max_length=64)
    mod_msg = models.ForeignKey(
        'Sms_Model',
        on_delete=models.CASCADE,
    )
    tel = models.CharField(max_length=13)
    validite = models.IntegerField(default=2)
    statut = models.CharField(max_length=16)
    loc = models.ForeignKey(
        'Geoloc',
        blank=True, null=True,
        on_delete=models.CASCADE,
    )
    envoi_hash = models.CharField(max_length=10)
    network = models.CharField(max_length=64, blank=True, null=True)

    def latitude(self):
        return self.point.y

    def longitude(self):
        return self.point.x

    def __str__(self):
    	return '{} - {:%d/%m/%Y %H:%M} - {}'.format(self.pk, self.dt_envoi, self.tel)

    class Meta:
        managed = True
        db_table = 'sms'


class Sms_Model(models.Model):
    nom = models.CharField(max_length=16)
    langue = models.CharField(max_length=4)
    texte = models.CharField(max_length=128)

    def __str__(self):
    	return self.nom + ' - ' + self.langue

    class Meta:
        managed = True
        db_table = 'sms_model'


class Geoloc(models.Model):
    dt_geoloc = models.DateTimeField(auto_now_add=True)
    origine = models.ForeignKey(
        'Sms',
        on_delete=models.CASCADE,
    )
    precision = models.IntegerField()
    geom = models.PointField(blank=True, null=True)
    ua = models.CharField(max_length=255, blank=True, null=True)

    def latitude(self):
        return self.point.y

    def longitude(self):
        return self.point.x

    def __str__(self):
    	#return '%s : %s' % (self.dt_geoloc, self.origine)
    	return '{} - {:%d/%m/%Y %H:%M} - {} - {} - {}m'.format(self.pk, self.dt_geoloc, self.origine, self.geom, self.precision)

    class Meta:
        managed = True
        db_table = 'geoloc'

