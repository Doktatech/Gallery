# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-16 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20190616_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo_image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
