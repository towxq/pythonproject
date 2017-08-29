# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256, verbose_name='\u6807\u9898')),
                ('author', models.CharField(default='', max_length=50, verbose_name='\u4f5c\u8005')),
                ('content', models.TextField(blank=True, default='', verbose_name='\u5185\u5bb9')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['createtime'],
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
        ),
    ]
