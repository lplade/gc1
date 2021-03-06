# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ebook_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.Creator')),
            ],
        ),
    ]
