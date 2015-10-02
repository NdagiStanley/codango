# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0009_auto_20150929_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\IniOluwa Fageyinbo\\Documents\\projects\\codango\\codango'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
