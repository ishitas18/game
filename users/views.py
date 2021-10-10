from django.shortcuts import render
from django.views.generic import TemplateView

from .models import UserScore
from levels.models import Levels, Medals

# Create your views here.
class UserScoreDetails(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = UserScore.objects.all()
        context['medals'] = Medals.objects.all()
        res = []
        count = 1
        for user in users:
            count += 1
            res.append({ 'x': count*5, 'y': user.score, 'name': user.user.name, 'medal': user.medal.name if user.medal else "None", 'level': user.level.name if user.level else "None" })
        context['data'] = res
        return context
