# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-06 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0030_auto_20180906_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='year',
            field=models.CharField(default='2018', max_length=4, verbose_name='Ano'),
        ),
    ]
