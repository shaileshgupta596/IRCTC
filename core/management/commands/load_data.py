from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Load Data in Backend"

    def handle(self, *args: Any, **options: Any) -> str | None:
        print("Load Data ....")