from django.core.management.base import BaseCommand

from users.models import User, UserScore
from levels.models import Levels, Medals


users = [{
        "name": "test01",
        "email": "test0001@yopmail.com",
        "score": 50
    },
    {
        "name": "test2",
        "email": "test2@yopmail.com",
        "score": 70
    },
    {
        "name": "test3",
        "email": "test3@yopmail.com",
        "score": 350
    },
    {
        "name": "test4",
        "email": "test4@yopmail.com",
        "score": 160
    },
    {
        "name": "test5",
        "email": "test5@yopmail.com",
        "score": 210
    },
    {
        "name": "test6",
        "email": "test6@yopmail.com",
        "score": 260
    },
    {
        "name": "test7",
        "email": "test7@yopmail.com",
        "score": 450
    }]


def load_user():
    for user in users:
        user_obj = User.objects.create(
            email=  user["email"],
            name=user["name"]
            )
        medals = Medals.objects.filter(min_level__lte=user["score"])
        levels = Levels.objects.filter(max_score__lte=user["score"])
        UserScore.objects.create(user=user_obj, score=user["score"], medal=medals[0] if medals else None, level=levels[0] if levels else None)

    print("Created users")


class Command(BaseCommand):
    def handle(self, **options):
        load_user()
