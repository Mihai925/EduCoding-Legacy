# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('cls_id', models.AutoField(serialize=False, verbose_name=b'ClassManagement id', primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'ClassManagement Name')),
                ('description', models.CharField(max_length=100, verbose_name=b'ClassManagement Description')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('teacher', models.ManyToManyField(related_name='teacher', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
