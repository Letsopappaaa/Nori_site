# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170417_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='post_dimensions',
            field=models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='1x1', max_length=15),
        ),
    ]