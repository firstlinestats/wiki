# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Definition(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    definition = models.TextField(null=True, blank=True)
    short_definition = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=10, null=True, blank=True)
    equation = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name
