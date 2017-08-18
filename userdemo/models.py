# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.CharField(max_length=50,primary_key='True')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telnumber = models.CharField(max_length=50)
    createtime = models.DateTimeField(auto_now_add=True)
    userrole = models.CharField(max_length=2)