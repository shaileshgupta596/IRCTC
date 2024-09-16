from django.contrib import admin
from trip.models import TrainSeatAvailable

# Register your models here.

@admin.register(TrainSeatAvailable)
class TrainSeatAdminForm(admin.ModelAdmin):
    pass
