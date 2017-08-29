# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from DjangoUeditor.forms import UEditorField

class blog(models.Model):
    title = models.CharField('标题',max_length=256,default='')
    author = models.CharField('作者',max_length=50,default='')
    content = models.TextField('内容',default='',blank=True)
    # content=UEditorField(u'内容	',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    # content = UEditorField('内容', height=300, width=1000,default=u'', blank=True, imagePath="uploads/images/",toolbars='besttome', filePath='uploads/files/')
    createtime = models.DateTimeField('创建时间',auto_now_add=True, editable=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '博客'
        ordering = ['createtime']

    def __unicode__(self):
        return self.title

# python manage.py startapp blog 创建模块

# python manage.py makemigrations blog
# python manage.py migrate
#  创建表
