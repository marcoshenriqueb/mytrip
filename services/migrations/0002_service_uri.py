# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='uri',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Endereço'),
        ),
    ]