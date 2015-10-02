# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_auto_20150916_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='author',
        ),
        migrations.AddField(
            model_name='resource',
            name='link',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\IniOluwa Fageyinbo\\Documents\\projects\\codango\\codango', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(default=b'CODE', max_length=30, choices=[(b'PDF', b'PDF Document'), (b'CODE', b'Code Snippet'), (b'LINK', b'Resource URL'), (b'IMAGE', b'Image file'), (b'VIDEO', b'Video file')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
