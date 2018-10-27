# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from .forms import AlgoForm


class CreateAlgoView(View):
    template_name = 'trades/create-algo.html'
    def get(self, request, *args, **kwargs):
        algo_form = AlgoForm()
        context = {
            'algo_form': algo_form
        }
        return render(request, self.template_name, context)
