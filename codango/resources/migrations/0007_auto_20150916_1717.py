# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20150916_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='name',
            new_name='title',
        ),
    ]
