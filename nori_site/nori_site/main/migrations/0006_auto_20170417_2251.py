# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_upload_post_dimensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='post_dimensions',
            field=models.CharField(choices=[('1x1', '1x1'), ('1x2', '1x2'), ('1x3', '1x3'), ('2x2', '2x2'), ('2x3', '2x3')], default='1x1', max_length=15),
        ),
    ]
