# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birth_date',
            new_name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='graduate',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='keywords',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nation',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
