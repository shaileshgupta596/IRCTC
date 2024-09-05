from django.db import models


class CoachTypeChoice(models.TextChoices):
    SLEEPER = 'SL', 'Sleeper'
    GENERAL = 'GN', 'General'
    LUGGAGE = 'LG', 'Luggage'
    PANTRY = 'PT', 'Pantry'
    GENERATOR = 'GEN', 'Generator'
    AC3 = 'AC3', 'AirConditioner 3'
    AC2 = 'AC2', 'AirConditioner 2'
    FIRSTCLASS = 'H', 'FIRSTCLASS'


class CoachGenerationType(models.TextChoices):
    VANDE_BHARAT = 'VB', 'Vande Bharat'
    LHB = 'LHB', 'LHB'
    ICF = 'ICF', 'ICF'
    DOUBLE_DECKAR = 'DD', 'Double Decker'