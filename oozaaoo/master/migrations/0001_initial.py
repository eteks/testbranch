# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccomodationStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('accomodation_star', models.CharField(max_length=50, verbose_name='Accomodation in Star Hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccomodationStarAndType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accomodation_star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.AccomodationStar')),
            ],
        ),
        migrations.CreateModel(
            name='AccomodationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('accomodation_type', models.CharField(max_length=50, verbose_name='Accomodation Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModeOfTransport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('transport_mode', models.CharField(max_length=50, verbose_name='Mode of Transport Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('transport_type', models.CharField(max_length=100, verbose_name='Transport Type')),
                ('transport_mode', models.ManyToManyField(to='master.ModeOfTransport', verbose_name='Transport Mode')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='accomodationstarandtype',
            name='accomodation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.AccomodationType'),
        ),
        migrations.AddField(
            model_name='accomodationstar',
            name='accomodation_type',
            field=models.ManyToManyField(through='master.AccomodationStarAndType', to='master.AccomodationType', verbose_name='Accomodation Type'),
        ),
    ]