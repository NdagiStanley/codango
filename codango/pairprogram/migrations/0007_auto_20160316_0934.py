# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0006_auto_20160120_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='session',
            field=models.ForeignKey(related_name='sessions', to='pairprogram.Session'),
        ),
    ]
