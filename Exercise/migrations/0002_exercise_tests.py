# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Autotester', '0001_initial'),
        ('Exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='tests',
            field=models.ManyToManyField(to='Autotester.ExerciseTests', blank=True),
            preserve_default=True,
        ),
    ]
