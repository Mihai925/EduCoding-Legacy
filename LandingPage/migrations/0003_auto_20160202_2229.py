# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0002_auto_20150327_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100, verbose_name=b'Author')),
                ('text', models.TextField(verbose_name=b'Text')),
                ('picture', models.ImageField(upload_to=b'author_pictures/', verbose_name=b'Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='quotes',
            field=models.ManyToManyField(related_name='Quptes', to='LandingPage.Quotes'),
            preserve_default=True,
        ),
    ]
