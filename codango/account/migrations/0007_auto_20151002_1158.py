# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20151002_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(default=b'image/upload/v1443782603/vqr7n59zfxyeybttleug.gif', max_length=255, verbose_name=b'image'),
        ),
    ]
