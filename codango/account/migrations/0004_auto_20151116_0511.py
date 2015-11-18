# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20151111_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='followed_id',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
