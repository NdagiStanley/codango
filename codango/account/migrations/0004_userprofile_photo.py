# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150922_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(default=datetime.datetime(2015, 9, 23, 17, 9, 43, 982000, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
