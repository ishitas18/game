from django.core.management.base import BaseCommand

from levels.models import Levels

levels = [{
        "name": "First",
        "max_score": 100
    },
    {
        "name": "Second",
        "max_score": 150
    },
    {
        "name": "Third",
        "max_score": 250
    },
    {
        "name": "Forth",
        "max_score": 400
    }]


def load_level():
    for level in levels:
        Levels.objects.update_or_create(name=level["name"], defaults={
            "name": level["name"],
            "max_score":level["max_score"]
            }
            )
    print("Created levels")


class Command(BaseCommand):
    def handle(self, **options):
        load_level()
