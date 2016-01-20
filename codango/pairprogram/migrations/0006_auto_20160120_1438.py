# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0005_auto_20151218_1154'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('participant', 'session')]),
        ),
    ]
