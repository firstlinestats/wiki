# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from terms.models import Definition


# Register your models here.
class DefinitionAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_definition', 'source', 'equation']


admin.site.register(Definition, DefinitionAdmin)
