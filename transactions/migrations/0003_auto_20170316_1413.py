# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-16 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20160927_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='envelope',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='envelopes.Envelope'),
        ),
    ]
