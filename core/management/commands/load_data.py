from typing import Any
from django.core.management.base import BaseCommand
import requests
from django.settings import BASE_DIR

class Command(BaseCommand):
    help = "Load Data in Backend"

    def handle(self, *args: Any, **options: Any) -> str | None:
        pass