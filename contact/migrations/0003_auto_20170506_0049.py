# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20170506_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=10000),
        ),
    ]
