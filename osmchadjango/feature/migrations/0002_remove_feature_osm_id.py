# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 10:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='osm_id',
        ),
    ]
