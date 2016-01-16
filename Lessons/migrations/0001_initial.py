# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.AutoField(serialize=False, verbose_name=b'Lesson ID', primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Lesson Title')),
                ('chapter_title', models.CharField(max_length=100, verbose_name=b'Chapter Title')),
                ('course_title', models.CharField(max_length=100, verbose_name=b'Course Title')),
                ('lesson_path', models.CharField(max_length=500, verbose_name=b'Path to Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
