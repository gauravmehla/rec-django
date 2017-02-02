# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150904_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allsubjects',
            name='semester',
            field=models.CharField(max_length=100, choices=[(b'First_Sem', b'1st'), (b'Second_Sem', b'2nd'), (b'Third_Sem', b'3rd'), (b'Fourth_Sem', b'4th'), (b'Fifth_Sem', b'5th'), (b'Sixth_Sem', b'6th'), (b'Seventh_Sem', b'7th'), (b'Eighth_Sem', b'8th')]),
        ),
    ]
