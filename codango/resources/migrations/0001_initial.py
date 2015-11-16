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
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True)),
                ('language_tags', models.CharField(default=b'Untagged', max_length=30, choices=[(b'PYTHON', b'Python'), (b'RUBY', b'Ruby'), (b'ANDROID', b'Android'), (b'MARKUP', b'HTML/CSS'), (b'JAVA', b'Java'), (b'PHP', b'PHP'), (b'IOS', b'IOS'), (b'JS', b'Javascript'), (b'C', b'C')])),
                ('resource_file', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'resource_file', blank=True)),
                ('resource_file_name', models.CharField(max_length=100, null=True)),
                ('resource_file_size', models.IntegerField(default=0)),
                ('snippet_text', models.TextField(null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
