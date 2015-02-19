# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finished',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished_description', models.CharField(max_length=400)),
                ('date_started', models.DateTimeField(verbose_name=b'date finished')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=400)),
                ('date_started', models.DateTimeField(verbose_name=b'date started')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('todo_description', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('join_date', models.DateTimeField(verbose_name=b'date finished')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(to='board.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inprogress',
            name='user',
            field=models.ForeignKey(to='board.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='finished',
            name='user',
            field=models.ForeignKey(to='board.User'),
            preserve_default=True,
        ),
    ]
