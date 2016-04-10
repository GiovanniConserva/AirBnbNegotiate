# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Negot', '0004_auto_20160403_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('airBnbId', models.FloatField(max_length=254, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('picture_url', models.URLField(max_length=254)),
                ('host_url', models.URLField(max_length=254)),
                ('host_name', models.CharField(max_length=254)),
                ('latitude', models.FloatField(max_length=254)),
                ('longitude', models.FloatField(max_length=254)),
                ('room_type', models.CharField(choices=[('Entire home/apt', 'Entire home/apt'), ('Private room', 'Private room'), ('Shared room', 'Shared room')], max_length=20)),
                ('price', models.FloatField()),
                ('minimum_nights', models.IntegerField()),
                ('number_of_reviews', models.IntegerField()),
                ('review_scores_rating', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='search',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Negot.User'),
        ),
        migrations.AddField(
            model_name='availability',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Negot.Listing'),
        ),
    ]