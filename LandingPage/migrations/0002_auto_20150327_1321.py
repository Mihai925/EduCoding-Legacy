# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='glyphicon',
            new_name='icon',
        ),
    ]
