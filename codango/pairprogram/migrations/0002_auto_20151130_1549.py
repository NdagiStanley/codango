# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairprogram',
            name='session_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pairprogram',
            name='initiator',
            field=models.ForeignKey(related_name='initiator', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='pairprogram',
            name='session_id',
            field=models.CharField(max_length=100),
        ),
    ]
