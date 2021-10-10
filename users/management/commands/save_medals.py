from django.core.management.base import BaseCommand

from levels.models import Medals

medals = [{
        "name": "Bronze",
        "min_level": 150
    },
    {
        "name": "Silver",
        "min_level": 250
    },
    {
        "name": "Premium",
        "min_level": 350
    }]


def load_medal():
    for medal in medals:
        Medals.objects.update_or_create(min_level=medal["min_level"], defaults={
            "name": medal["name"],
            "min_level":medal["min_level"]
            }
        )
    print("Created Medals")


class Command(BaseCommand):
    def handle(self, **options):
        load_medal()
