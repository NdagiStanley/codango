# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_follow', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(related_name='following', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(related_name='languages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=200, null=True)),
                ('activity_type', models.CharField(max_length=50)),
                ('read', models.BooleanField()),
                ('content', models.TextField(max_length=1200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('social_id', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('place_of_work', models.CharField(max_length=150, blank=True)),
                ('position', models.CharField(max_length=100, blank=True)),
                ('about', models.TextField(max_length=1200, blank=True)),
                ('github_username', models.CharField(max_length=200, null=True)),
                ('frequency', models.CharField(default=b'none', max_length=200)),
                ('image', cloudinary.models.CloudinaryField(default=b'image/upload/v1443782603/vqr7n59zfxyeybttleug.gif', max_length=255, verbose_name=b'image')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'followed')]),
        ),
    ]
