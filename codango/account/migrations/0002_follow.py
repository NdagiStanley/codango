# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followed_id', models.IntegerField()),
                ('date_of_follow', models.DateTimeField(auto_now_add=True)),
                ('follower_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
