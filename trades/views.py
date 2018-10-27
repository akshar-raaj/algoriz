# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class CreateAlgoView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Create Algo page")
