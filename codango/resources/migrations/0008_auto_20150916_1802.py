# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_auto_20150916_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(null=True, upload_to=b'/resources'),
        ),
    ]
