# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20151110_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='upvotes',
        ),
    ]
