# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20151001_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(default=b'image/upload/v1443782199/pi5h0e35iq9kwlqo0vze.jpg', max_length=255, verbose_name=b'image'),
        ),
    ]
