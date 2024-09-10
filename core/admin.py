from django.contrib import admin

from core.models import Train, TrainCoaches, TrainHalts

# Register your models here.



@admin.register(TrainCoaches)
class TrainCoachesAdminForm(admin.ModelAdmin):
    list_display = ['train', 'number', 'name', 'type']


@admin.register(Train)
class TrainAdminForm(admin.ModelAdmin):
    pass


@admin.register(TrainHalts)
class TrainHaltAdminForm(admin.ModelAdmin):
    pass