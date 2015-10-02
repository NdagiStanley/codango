# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import cloudinary.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0015_auto_20151001_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='snippet_text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='language_tags',
            field=models.CharField(default=b'Untagged', max_length=30, choices=[(b'PYTHON', b'Python'), (b'RUBY', b'Ruby'), (b'ANDROID', b'Android'), (b'MARKUP', b'HTML/CSS'), (b'JAVA', b'Java'), (b'PHP', b'PHP'), (b'IOS', b'IOS'), (b'JS', b'Javascript'), (b'C', b'C')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=cloudinary.models.CloudinaryField(default=datetime.datetime(2015, 10, 2, 12, 8, 27, 537000, tzinfo=utc), max_length=255, verbose_name=b'resource_file'),
            preserve_default=False,
        ),
    ]
