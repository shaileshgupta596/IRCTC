from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.choices import CoachTypeChoice, CoachGenerationType

from core.choices import (CoachGenerationType as CGT,    
                        CoachTypeChoice as CTC)
from core.configurations.coach_configurations import *

from station.models import Station


class TrainModelQuerySet(models.QuerySet):
    def train_between_stations(self, source=None, destination=None):
        return self.filter(
            source__icontains=source,
            destination__icontains=destination
        )


class TrainModelManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return TrainModelQuerySet(self.model, using=self._db)
    
    def train_between_stations(self, source, destination):
        return self.get_queryset().train_between_stations(source, destination)


class Train(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.CharField(max_length=5, unique=True)
    source = models.CharField(max_length=200)
    source_station_code = models.CharField(max_length=5)
    destination = models.CharField(max_length=200)
    destination_station_code = models.CharField(max_length=5)

    objects = TrainModelManager()

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.number} - {self.name}"
    

class TrainHalts(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_halts')
    halts = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_halts')
    at_halt = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.train.number} - {self.halts.name}'

    

class TrainCoaches(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=5)
    type = models.CharField(max_length=5, choices=CTC)
    generation = models.CharField(max_length=5, choices=CGT)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_coaches')
    number_of_seats = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    


@receiver(signal=pre_save, sender=TrainCoaches)
def train_coaches_pre_save_handler(sender, instance, *args, **kwargs):
    if not instance.number_of_seats:
        if instance.generation == CGT.ICF and instance.type == CTC.SLEEPER:
            instance.number_of_seats = ICF_SLEEPER

        elif instance.generation == CGT.ICF and instance.type == CTC.AC3:
            instance.number_of_seats = ICF_AC3

        elif instance.generation == CGT.ICF and instance.type == CTC.AC2:
            instance.number_of_seats = ICF_AC2

        elif instance.generation == CGT.ICF and instance.type == CTC.FIRSTCLASS:
            instance.number_of_seats = ICF_FIRSTCLASS

        elif instance.generation == CGT.LHB and instance.type == CTC.SLEEPER:
            instance.number_of_seats = LHB_SLEEPER

        elif instance.generation == CGT.LHB and instance.type == CTC.AC3:
            instance.number_of_seats = LHB_AC3

        elif instance.generation == CGT.choices.LHB and instance.type == CTC.AC2:
            instance.number_of_seats = LHB_AC2

        elif instance.generation == CGT.choices.LHB and instance.type == CTC.FIRSTCLASS:
            instance.number_of_seats = LHB_FIRSTCLASS

        elif instance.generation == CGT.VANDE_BHARAT and instance.type == CTC.CHAIRCAR:
            instance.number_of_seats = VANDE_BHARAT_CHAIRCAR

        elif instance.generation == CGT.VANDE_BHARAT and instance.type == CTC.EXECUTIVECLASS:
            instance.number_of_seats = VANDE_BHARAT_EXECUTIVECLASS

        elif instance.generation == CGT.DOUBLE_DECKAR and instance.type == CTC.CHAIRCAR:
            instance.number_of_seats = DOUBLE_DECKAR_CHAIRCAR

        elif instance.generation == CGT.DOUBLE_DECKAR and instance.type == CTC.EXECUTIVECLASS:
            instance.number_of_seats = DOUBLE_DECKAR_EXECUTIVECLASS
        
        else:
            instance.number_of_seats = 0


    


    

