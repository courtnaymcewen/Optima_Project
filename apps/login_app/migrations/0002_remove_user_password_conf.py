# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-07 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_conf',
        ),
    ]
