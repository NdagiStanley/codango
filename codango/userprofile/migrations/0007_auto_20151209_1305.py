# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0006_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=200, null=True)),
                ('activity_type', models.CharField(max_length=50)),
                ('read', models.BooleanField()),
                ('content', models.TextField(max_length=1200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='user',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]
