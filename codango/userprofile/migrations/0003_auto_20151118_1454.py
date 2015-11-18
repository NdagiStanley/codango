# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20151118_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='fb_id',
            new_name='social_id',
        ),
    ]
