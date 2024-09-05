from django.db import models
from core.choices import CoachTypeChoice, CoachGenerationType


class Train(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.CharField(max_length=5, unique=True)
    source = models.CharField(max_length=200)
    source_station_code = models.CharField(max_length=5)
    destination = models.CharField(max_length=200)
    destination_station_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.number} - {self.name}"
    

class TrainCoaches(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=5)
    type = models.CharField(max_length=5, choices=CoachTypeChoice.choices)
    generation = models.CharField(max_length=5, choices=CoachGenerationType.choices)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    number_of_seats = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name

    

