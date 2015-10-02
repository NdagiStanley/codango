# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_auto_20150929_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='link',
        ),
        migrations.AlterField(
            model_name='resource',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 29, 19, 3, 49, 261000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(default='', upload_to=b'C:\\Users\\IniOluwa Fageyinbo\\Documents\\projects\\codango\\codango'),
            preserve_default=False,
        ),
    ]
