# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from userdemo.models import User


class userAdmin(admin.ModelAdmin):
    list_display = ('username','password','telnumber','createtime','userrole')

admin.site.register(User,userAdmin)