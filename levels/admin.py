from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Levels)
admin.site.register(Medals)
