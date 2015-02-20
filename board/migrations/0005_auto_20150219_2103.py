# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20150218_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(verbose_name=b'date joined'),
            preserve_default=True,
        ),
    ]
