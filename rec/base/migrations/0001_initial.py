# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Classes List',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(serialize=False, primary_key=True)),
                ('department_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Department List',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('teacher_id', models.AutoField(serialize=False, primary_key=True)),
                ('teacher_name', models.CharField(max_length=255)),
                ('teacher_dept', models.ForeignKey(to='base.Department')),
            ],
            options={
                'verbose_name_plural': 'Teachers List',
            },
        ),
    ]
