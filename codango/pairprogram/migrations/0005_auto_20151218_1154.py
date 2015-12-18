# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0004_auto_20151216_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='joined_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='session',
            name='last_active_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
