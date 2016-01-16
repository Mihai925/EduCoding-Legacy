# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Class', '0003_invitation_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationModel',
            fields=[
                ('invitation_id', models.AutoField(serialize=False, verbose_name=b'Invitation id', primary_key=True)),
                ('student_email', models.CharField(max_length=100, verbose_name=b'Student Email')),
                ('invitation_code', models.CharField(max_length=100, verbose_name=b'Invitation Code')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, auto_now=True)),
                ('class_to_add', models.ForeignKey(blank=True, to='Class.Class', null=True)),
                ('teacher', models.ForeignKey(related_name='Teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='class_to_add',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
        migrations.AlterUniqueTogether(
            name='invitationmodel',
            unique_together=set([('invitation_code',)]),
        ),
    ]
