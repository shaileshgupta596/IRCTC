from django.contrib import admin

from station.models import Station, StationRoute

# Register your models here.

@admin.register(Station)
class StationAdminForm(admin.ModelAdmin):
    pass


@admin.register(StationRoute)
class StationRouteAdminForm(admin.ModelAdmin):
    pass
