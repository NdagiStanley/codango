# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='language_tags',
            field=models.CharField(default=b'Untagged', max_length=30, choices=[(b'PYTHON', b'Python'), (b'RUBY', b'Ruby'), (b'ANDROID', b'Android'), (b'MARKUP', b'HTML/CSS'), (b'JAVA', b'Java'), (b'PHP', b'PHP'), (b'IOS', b'IOS'), (b'JAVASCRIPT', b'Javascript'), (b'C', b'C')]),
        ),
    ]
