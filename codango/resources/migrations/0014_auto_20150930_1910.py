# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_auto_20150929_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='title',
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(null=True, upload_to=b'pdf', blank=True),
        ),
    ]
