import random
import json
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

from core.models import Train, TrainCoaches
from core.choices import CoachTypeChoice, CoachGenerationType



class Command(BaseCommand):
    help = "Command to load coach details for Trains"

    def handle(self, *args: Any, **options: Any) -> str | None:
        TrainCoaches.objects.all().delete()

        trains = Train.objects.all()

        with open(settings.BASE_DIR/"core/data/coach_config.json", 'r') as f:
            express_types = json.loads(f.read())

        for train in trains:
            express_type = train.express_type
            coach_config = express_types.get(express_type)
            coach_number = 1
            for coach_type, number in coach_config.items():
               for i in range(1, number+1):
                   train_coach = TrainCoaches(
                       number = coach_number,
                       name= f"{coach_type}{i}",
                       type=coach_type,
                       generation='LHB',
                       train=train
                   ) 
                   train_coach.save()

                   coach_number += 1
        print(f"Loaded Information for {TrainCoaches.objects.count()}")

            