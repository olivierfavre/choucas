from django.contrib import admin

# Register your models here.

from django.conf import settings
from leaflet.admin import LeafletGeoAdmin
from gendloc.models import Sms
from gendloc.models import Sms_Model
from gendloc.models import Geoloc

class MapLeafletGeoAdmin(LeafletGeoAdmin):
# straight hint @https://github.com/makinacorpus/django-leaflet/pull/28#issuecomment-23943492
    settings_overrides = {
    	'TILES': [
			('IGN Maps', settings.SCAN_IGN, settings.IGN_ATTRIB),
			('IGN Ortho', settings.ORTHO_IGN, settings.IGN_ATTRIB),
			('OSM', settings.BASE_OSM, settings.OSM_ATTRIB),
		],    
		#'MINIMAP': True,
	}    

admin.site.register(Sms)
admin.site.register(Sms_Model)
admin.site.register(Geoloc, MapLeafletGeoAdmin)
