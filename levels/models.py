from django.db import models

# Create your models here.
class Levels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, unique=True)
    max_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Medals(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    min_level = models.PositiveIntegerField(default=0, unique=True)

    def __str__(self):
        return self.name