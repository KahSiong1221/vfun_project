from django.contrib.gis import admin
from .models import Profile, SportsHall

admin.site.register(Profile)
admin.site.register(SportsHall, admin.OSMGeoAdmin)
