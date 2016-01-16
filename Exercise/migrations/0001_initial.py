# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('ex_id', models.AutoField(serialize=False, verbose_name=b'Exercise ID', primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('content', models.TextField(verbose_name=b'Content')),
                ('classes_assigned_to', models.ManyToManyField(to='Class.Class', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
