# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='class_dept',
            field=models.ForeignKey(default=2, to='base.Department'),
            preserve_default=False,
        ),
    ]
