# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20150829_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
