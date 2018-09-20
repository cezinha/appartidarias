# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-29 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0026_auto_20160927_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total recebido')),
                ('paid', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total Gasto')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='state',
            field=models.CharField(default='BR', max_length=100, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate', verbose_name='Candidata'),
        ),
    ]