import random
from typing import Any
from django.core.management.base import BaseCommand

from core.models import Train, TrainCoaches
from core.choices import CoachTypeChoice, CoachGenerationType

class Command(BaseCommand):
    help = "Command to load coach details for Trains"

    def handle(self, *args: Any, **options: Any) -> str | None:
        TrainCoaches.objects.all().delete()

        trains = Train.objects.all()

        
        for train in trains:
            total_general_coach = 4

            coach_number = 1
            coach_generation = random.choice([CoachGenerationType.ICF, CoachGenerationType.LHB])
            TrainCoaches(
                number=coach_number,
                name='GEN1',
                type=CoachTypeChoice.GENERATOR,
                generation=coach_generation,
                train=train
            )

            general_coach = random.randint(1, 4)
            remaing_general_coach = total_general_coach - general_coach

            for _ in range(general_coach):
                coach_number += 1
                TrainCoaches(
                    number=coach_number,
                    name='GEN2',
                    type=CoachTypeChoice.GENERATOR,
                    generation=coach_generation,
                    train=train
                )

            for _ in range(remaing_general_coach):
                coach_number += 1
                TrainCoaches(
                    number=coach_number,
                    name='GEN2',
                    type=CoachTypeChoice.GENERATOR,
                    generation=coach_generation,
                    train=train
                )


            TrainCoaches(
                number=coach_number,
                name='GEN2',
                type=CoachTypeChoice.GENERATOR,
                generation=coach_generation,
                train=train
            )