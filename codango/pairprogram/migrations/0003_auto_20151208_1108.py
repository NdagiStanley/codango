# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pairprogram', '0002_auto_20151130_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('joined_date', models.DateTimeField(verbose_name=datetime.datetime(2015, 12, 8, 10, 8, 55, 405340, tzinfo=utc))),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_name', models.CharField(max_length=200, null=True)),
                ('last_active_date', models.DateTimeField(verbose_name=datetime.datetime(2015, 12, 8, 10, 8, 55, 403903, tzinfo=utc))),
                ('status', models.BooleanField(default=True)),
                ('initiator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pairprogram',
            name='initiator',
        ),
        migrations.DeleteModel(
            name='PairProgram',
        ),
        migrations.AddField(
            model_name='participant',
            name='session_id',
            field=models.ForeignKey(to='pairprogram.Session'),
        ),
    ]
