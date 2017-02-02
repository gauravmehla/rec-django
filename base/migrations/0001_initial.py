# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllSubjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.CharField(max_length=100, choices=[(b'First_Sem', b'1st'), (b'Second_Sem', b'2nd'), (b'Third_Sem', b'3rd'), (b'Fourth_Sem', b'4th'), (b'Fifth_Sem', b'5th'), (b'Sixth_sem', b'6th'), (b'Seventh_Sem', b'7th'), (b'Eighth_Sem', b'8th')])),
                ('subject_1', models.CharField(max_length=100, blank=True)),
                ('subject_2', models.CharField(max_length=100, blank=True)),
                ('subject_3', models.CharField(max_length=100, blank=True)),
                ('subject_4', models.CharField(max_length=100, blank=True)),
                ('subject_5', models.CharField(max_length=100, blank=True)),
                ('subject_6', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'verbose_name_plural': 'All Subjects List',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(unique=True, max_length=100)),
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
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=30)),
                ('group_dept', models.ForeignKey(to='base.Department')),
            ],
            options={
                'verbose_name_plural': 'Groups List',
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
        migrations.AddField(
            model_name='classes',
            name='class_dept',
            field=models.ForeignKey(to='base.Department'),
        ),
        migrations.AddField(
            model_name='allsubjects',
            name='class_for',
            field=models.ForeignKey(to='base.Classes'),
        ),
    ]
