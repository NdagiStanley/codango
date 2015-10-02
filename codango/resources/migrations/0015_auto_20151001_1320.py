# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_auto_20150930_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='resource_type',
        ),
        migrations.AddField(
            model_name='resource',
            name='language_tags',
            field=models.CharField(default=b'PYTHON', max_length=30, choices=[(b'PYTHON', b'Python'), (b'RUBY', b'Ruby')]),
        ),
    ]
