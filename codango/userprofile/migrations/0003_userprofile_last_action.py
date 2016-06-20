# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20160606_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_action',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 18, 5, 38, 39201)),
        ),
    ]
