# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170418_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='img_pos',
            field=models.CharField(choices=[('blog_img-10', '-10%'), ('blog_img-20', '-20%'), ('blog_img-30', '-30%'), ('blog_img-40', '-40%'), ('blog_img-50', '-50%'), ('blog_img-60', '-60%'), ('blog_img-70', '-70%'), ('blog_img-80', '-80%'), ('blog_img-90', '-90%')], default=None, max_length=10),
        ),
    ]