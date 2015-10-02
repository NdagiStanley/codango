# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20150901_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='resourcetype',
            new_name='resource_type',
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(default=datetime.datetime(2015, 9, 16, 16, 13, 5, 972000, tzinfo=utc), upload_to=b'/resources'),
            preserve_default=False,
        ),
    ]
