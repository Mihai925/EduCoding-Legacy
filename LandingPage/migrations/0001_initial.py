# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('glyphicon', models.CharField(max_length=100, verbose_name=b'Glyphicon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name=b'Description')),
                ('features', models.ManyToManyField(related_name='Features', to='LandingPage.Feature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
