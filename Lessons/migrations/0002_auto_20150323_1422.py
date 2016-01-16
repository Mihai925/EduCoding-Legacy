# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0001_initial'),
        ('Lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.AutoField(serialize=False, verbose_name=b'Unit ID', primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Unit Title')),
                ('lessons', models.ManyToManyField(to='Lessons.Lesson', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='chapter_title',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='course_title',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_path',
        ),
        migrations.AddField(
            model_name='lesson',
            name='assignments',
            field=models.ManyToManyField(to='Exercise.Exercise', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='briefing',
            field=models.TextField(default=b'', verbose_name=b'Briefing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Lesson Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='introduction',
            field=models.TextField(default=b'', verbose_name=b'Introduction'),
            preserve_default=True,
        ),
    ]
