# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20150831_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='resource',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='resourcetype',
            field=models.CharField(default=b'CODE', max_length=30, choices=[(b'PDF', b'PDF Document'), (b'CODE', b'Code Snippet'), (b'LINK', b'Resource URL')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='text',
            field=models.TextField(),
        ),
    ]
