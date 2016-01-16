# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseTests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input', models.CharField(max_length=500, verbose_name=b'Input')),
                ('expected_output', models.CharField(max_length=500, verbose_name=b'Output')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
