from django.db import models
from core.choices import IndianRailwayZone, IndianState, StationTypeChoice


class Station(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    number_of_platforms = models.IntegerField()
    type = models.CharField(max_length=2, choices=StationTypeChoice.choices)
    state = models.CharField(max_length=2, choices=IndianState.choices)
    zone = models.CharField(max_length=5, choices=IndianRailwayZone.choices)

    def __str__(self):
        return f'{self.code}-{self.name}'


class Train(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.CharField(max_length=5, unique=True)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.number} - {self.name}"