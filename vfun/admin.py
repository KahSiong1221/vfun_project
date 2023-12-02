from django.contrib.gis import admin
from .models import Profile, SportsHall, Session

admin.site.register(Profile)
admin.site.register(Session)
admin.site.register(SportsHall, admin.OSMGeoAdmin)
