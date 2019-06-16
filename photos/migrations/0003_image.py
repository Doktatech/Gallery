# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-16 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20190616_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50)),
                ('photo_image', models.ImageField(upload_to='photos/')),
                ('image_description', models.TextField()),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('image_location', models.CharField(max_length=60)),
                ('image_category', models.CharField(max_length=50)),
                ('tags', models.ManyToManyField(to='photos.tags')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Uploader')),
            ],
        ),
    ]