# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='followed_id',
            new_name='followed',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='follower_id',
            new_name='follower',
        ),
    ]
