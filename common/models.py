# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telnumber = models.CharField(max_length=50)
    createtime = models.DateTimeField(default=datetime.now)
    userrole = models.CharField(max_length=2)