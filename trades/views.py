# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class CreateAlgoView(View):
    template_name = 'trades/create-algo.html'
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, self.template_name, context)
