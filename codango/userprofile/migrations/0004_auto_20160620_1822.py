# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_last_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_action',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
