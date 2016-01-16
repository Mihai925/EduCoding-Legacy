# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('student_email', models.CharField(max_length=100, verbose_name=b'Student Email')),
                ('invitation_code', models.CharField(max_length=100, serialize=False, verbose_name=b'Invitation Code', primary_key=True)),
                ('class_to_add', models.ForeignKey(blank=True, to='Class.Class', null=True)),
                ('teacher', models.ForeignKey(related_name='Teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
