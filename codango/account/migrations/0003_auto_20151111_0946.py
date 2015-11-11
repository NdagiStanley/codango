# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='followed_id',
            field=models.ForeignKey(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follower_id',
            field=models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
