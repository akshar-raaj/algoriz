# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Algorithm(models.Model):
    name = models.CharField(max_length=100)
    positions = ArrayField(models.TextField(), null=True, blank=True, default=list)
    PnL = ArrayField(models.TextField(), null=True, blank=True, default=list)

    def __unicode__(self):
        return self.name

    def average(self):
        return sum([float(each) for each in self.PnL])/len(self.PnL)
