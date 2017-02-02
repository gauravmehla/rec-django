# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSE2016_attendence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stud_roll', models.IntegerField(unique=True)),
                ('stud_name', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=30, blank=True)),
                ('subjects', models.CharField(max_length=100, blank=True)),
                ('attendence', models.CharField(default=b'0|0|0|0|0|0', max_length=100, blank=True)),
                ('total', models.CharField(default=b'0|0|0|0|0|0', max_length=100, blank=True)),
                ('email_id', models.CharField(max_length=100, blank=True)),
                ('phone_no', models.CharField(max_length=12, blank=True)),
                ('group', models.ForeignKey(to='base.Groups')),
            ],
            options={
                'verbose_name_plural': 'CSE2016_attendence',
            },
        ),
        migrations.CreateModel(
            name='CSE2017_attendence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stud_roll', models.IntegerField(unique=True)),
                ('stud_name', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=30, blank=True)),
                ('subjects', models.CharField(max_length=100, blank=True)),
                ('attendence', models.CharField(default=b'0|0|0|0|0|0', max_length=100, blank=True)),
                ('total', models.CharField(default=b'0|0|0|0|0|0', max_length=100, blank=True)),
                ('email_id', models.CharField(max_length=100, blank=True)),
                ('phone_no', models.CharField(max_length=12, blank=True)),
                ('group', models.ForeignKey(to='base.Groups')),
            ],
            options={
                'verbose_name_plural': 'CSE2017_attendence',
            },
        ),
    ]
