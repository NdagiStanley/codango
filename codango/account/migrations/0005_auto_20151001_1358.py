# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import cloudinary.models
import account.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(default=datetime.datetime(2015, 10, 1, 12, 58, 38, 803000, tzinfo=utc), max_length=255, verbose_name=b'image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(upload_to=account.models.get_upload_file_name, blank=True),
        ),
    ]
