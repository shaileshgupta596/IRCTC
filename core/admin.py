from django.contrib import admin

from core.models import Station, Train

# Register your models here.

@admin.register(Station)
class StationAdminForm(admin.ModelAdmin):
    pass


@admin.register(Train)
class TrainAdminForm(admin.ModelAdmin):
    pass