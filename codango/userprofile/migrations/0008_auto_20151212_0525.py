# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20151209_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='notification',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
