# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('description_home', models.TextField(blank=True, null=True, verbose_name='Descrição home')),
                ('icon', models.ImageField(blank=True, max_length=255, null=True, upload_to='servicesicons/%Y/%m/%d/', verbose_name='Ícone')),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='servicesphotos/%Y/%m/%d/', verbose_name='Foto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]
