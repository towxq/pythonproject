# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from projectdemo.models import Project


class projectAdmin(admin.ModelAdmin):
    list_display = ('projectname','projecturl','projectdesc','projectcreatetime','projectupdatetime','bgColor')

admin.site.register(Project,projectAdmin)