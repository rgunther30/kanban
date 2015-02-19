# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20150218_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished',
            name='user',
            field=models.ForeignKey(related_name='finished_user', blank=True, to='board.User', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inprogress',
            name='user',
            field=models.ForeignKey(related_name='inprogress_user', blank=True, to='board.User', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(related_name='todo_user', blank=True, to='board.User', null=True),
            preserve_default=True,
        ),
    ]
