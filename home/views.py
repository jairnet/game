import random

from django.shortcuts import render
from django.views import View

from home.models import Gamer, Score
from . import rule

class index(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name', '')
        Gamer(name=name).save()
        print('obj_gamer', obj_gamer)
        return render(request, 'home/game.html', context={'name':name})

class game(View):
    template_name = 'home/game.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})
    
    def post(self, request, *args, **kwargs):
        gamer = ''
        piedra = self.request.POST.get('piedra', '')
        papel = self.request.POST.get('papel', '')
        tijera = self.request.POST.get('tijera', '')
        lagarto = self.request.POST.get('lagarto', '')
        spock = self.request.POST.get('spock', '')
        python_gamer = random.choice(
            ['Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock'])
        if piedra:
            gamer = '{0}-{1}'.format(piedra, python_gamer)
        if papel:
            gamer = '{0}-{1}'.format(papel, python_gamer)
        if tijera:
            gamer = '{0}-{1}'.format(tijera, python_gamer)
        if lagarto:
            gamer = '{0}-{1}'.format(lagarto, python_gamer)
        if spock:
            gamer = '{0}-{1}'.format(spock, python_gamer)
        score_tmp = rule.rules.get(gamer)
        context = {
            'power_python': python_gamer,
            'score_gamer': score_tmp[0],
            'score_python': score_tmp[1]
        }
        return render(request, self.template_name, context=context)
