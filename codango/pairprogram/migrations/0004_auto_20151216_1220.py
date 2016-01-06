# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0003_auto_20151208_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='session_id',
            new_name='session',
        ),
        migrations.AlterField(
            model_name='participant',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 16, 11, 20, 40, 217429, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='last_active_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 16, 11, 20, 40, 216577, tzinfo=utc)),
        ),
    ]
