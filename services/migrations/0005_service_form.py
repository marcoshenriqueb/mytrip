# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='form',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Form (não mudar)'),
        ),
    ]
