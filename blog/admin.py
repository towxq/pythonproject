# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blog.models import blog


class blogAdmin(admin.ModelAdmin):
    list_display = ('title','author','content','createtime','updatetime')

admin.site.register(blog,blogAdmin)
