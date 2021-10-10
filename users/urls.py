from django.urls import path

from .views import *


urlpatterns = [
    path('', UserScoreDetails.as_view(), name="home"),
]
