# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jus', '0007_auto_20170719_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='ju',
            name='items',
            field=models.TextField(default=''),
        ),
    ]
