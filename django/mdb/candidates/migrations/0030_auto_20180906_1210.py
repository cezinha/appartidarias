# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-06 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0029_auto_20180905_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='coalition',
            field=models.CharField(max_length=128, verbose_name='Coligação'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='education',
            field=models.CharField(max_length=128, verbose_name='Nível escolaridade'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='job',
            field=models.CharField(max_length=128, verbose_name='Ocupação'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='reelection',
            field=models.BooleanField(default=False, verbose_name='Re-eleição?'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('A', 'Aprovado'), ('D', 'Negado')], default='P', max_length=1, verbose_name='Aprovação candidatura MDB'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='jobrole',
            name='code',
            field=models.CharField(max_length=128, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='about',
            field=models.TextField(null=True, verbose_name='sobre'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='directory_city',
            field=models.TextField(blank=True, null=True, verbose_name='diretório municipal'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='directory_national',
            field=models.TextField(blank=True, null=True, verbose_name='diretório nacional'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='directory_state',
            field=models.TextField(blank=True, null=True, verbose_name='diretório estadual'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='initials',
            field=models.CharField(max_length=128, unique=True, verbose_name='sigla'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='number',
            field=models.IntegerField(unique=True, verbose_name='numero'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
