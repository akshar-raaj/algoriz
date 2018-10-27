# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from algoriz.services import pull_close_prices, algo_result
from .forms import AlgoForm
from .models import Algorithm


class CreateAlgoView(View):
    template_name = 'trades/create-algo.html'
    def get(self, request, *args, **kwargs):
        algo_form = AlgoForm()
        context = {
            'algo_form': algo_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        algo_form = AlgoForm(data=request.POST)
        if algo_form.is_valid():
            prices = pull_close_prices(algo_form.cleaned_data['ticker'])
            positions, PnL = algo_result(str(algo_form.cleaned_data['signal']), str(algo_form['trade']), prices)
            data = {
                'name': algo_form.cleaned_data['name'],
                'PnL': PnL,
                'positions': positions
            }
            algo = Algorithm.objects.create(**data)
            return HttpResponseRedirect('/trades/create-algo/')
        context = {
            'algo_form': algo_form
        }
        return render(request, self.template_name, context)


class AlgosView(TemplateView):
    template_name = 'trades/algos.html'

    def get_context_data(self, *args, **kwargs):
        algos = Algorithm.objects.all()
        return {
            'algos': algos
        }
