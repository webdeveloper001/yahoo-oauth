# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yahoo_leagues', '0002_auto_20170411_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='first_name',
            new_name='imageurl',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='full_name',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='username',
        ),
    ]
