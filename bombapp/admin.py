from django.contrib import admin
from .models import Airfields, BombSites
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class AirfieldsAdmin(LeafletGeoAdmin):
    ordering = ('airfieldName', 'groupId')
    list_display = ('airfieldName', 'groupName')
    
class BombSitesAdmin(LeafletGeoAdmin):
    ordering = ('opDate', 'groupId')
    list_display = ('opDate', 'place', 'target')
    
admin.site.register(Airfields, AirfieldsAdmin)
admin.site.register(BombSites, BombSitesAdmin)
    