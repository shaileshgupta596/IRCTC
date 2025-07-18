from django.db import models
from station.choices import IndianRailwayZone, IndianState, StationTypeChoice

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    number_of_platforms = models.IntegerField()
    type = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=IndianState.choices)
    zone = models.CharField(max_length=5, choices=IndianRailwayZone.choices)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'{self.code}-{self.name}'
    

class StationRoute(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    routes = models.ManyToManyField(Station, related_name='routes')

    def __str__(self):
        return self.station.name