# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150904_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSE2016_attendence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stud_roll', models.IntegerField(unique=True)),
                ('stud_name', models.CharField(max_length=100)),
                ('sem', models.CharField(blank=True, max_length=30, choices=[(b'First_Sem', b'1st'), (b'Second_Sem', b'2nd'), (b'Third_Sem', b'3rd'), (b'Fourth_Sem', b'4th'), (b'Fifth_Sem', b'5th'), (b'Sixth_Sem', b'6th'), (b'Seventh_Sem', b'7th'), (b'Eighth_Sem', b'8th')])),
                ('subjects', models.CharField(max_length=100, blank=True)),
                ('attendence', models.CharField(default=b'0|0|0|0|0|0', max_length=100, blank=True)),
                ('total', models.CharField(default=b'0|0|0|0|0|0', max_length=100, blank=True)),
                ('email_id', models.CharField(max_length=100, blank=True)),
                ('phone_no', models.CharField(max_length=100, blank=True)),
                ('group_name', models.ForeignKey(to='base.Groups')),
            ],
            options={
                'verbose_name_plural': 'CSE2016_attendence',
            },
        ),
    ]
