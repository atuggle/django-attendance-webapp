# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 22:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['event'],
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', regex='^\\+?1?\\d{8,15}$')])),
            ],
            options={
                'verbose_name_plural': 'Attendees',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='Title')),
                ('date_time', models.DateField(default=django.utils.timezone.now, verbose_name='Event date time')),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Attendee'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]