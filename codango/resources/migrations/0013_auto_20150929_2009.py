# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20150929_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_file',
            field=models.FileField(null=True, upload_to=b'C:\\Users\\IniOluwa Fageyinbo\\Documents\\projects\\codango\\codango', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
