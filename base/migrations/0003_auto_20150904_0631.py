# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_cse2016_attendence_cse2017_attendence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cse2016_attendence',
            name='group',
        ),
        migrations.RemoveField(
            model_name='cse2017_attendence',
            name='group',
        ),
        migrations.DeleteModel(
            name='CSE2016_attendence',
        ),
        migrations.DeleteModel(
            name='CSE2017_attendence',
        ),
    ]
