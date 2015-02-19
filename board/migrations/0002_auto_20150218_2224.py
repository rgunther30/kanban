# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished',
            name='user',
            field=models.ForeignKey(related_name='finished_user', to='board.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inprogress',
            name='user',
            field=models.ForeignKey(related_name='inprogress_user', to='board.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(related_name='todo_user', to='board.User'),
            preserve_default=True,
        ),
    ]
