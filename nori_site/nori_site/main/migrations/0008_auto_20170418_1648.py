# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170418_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
    ]
