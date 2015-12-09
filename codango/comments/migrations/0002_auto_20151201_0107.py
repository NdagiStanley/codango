# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 0, 7, 32, 454000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
