# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Negot', '0002_auto_20160402_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='chechout_date',
            field=models.DateField(verbose_name='%d %b, %Y'),
        ),
        migrations.AlterField(
            model_name='search',
            name='checkin_date',
            field=models.DateField(verbose_name='%d %b, %Y'),
        ),
        migrations.AlterField(
            model_name='search',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Negot.User'),
        ),
    ]
