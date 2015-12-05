# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20151118_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='github_username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
