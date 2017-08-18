# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    class Meta:
        db_table = 'project'

    id = models.CharField(max_length=50,primary_key='True')
    projectname = models.CharField(max_length=50)
    projecturl = models.CharField(max_length=200)
    projectdesc = models.CharField(max_length=200)
    projectcreatetime = models.DateTimeField(auto_now_add=True)
    projectupdatetime = models.DateTimeField(auto_now_add=True)
    bgColor = models.CharField(max_length=20)