# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='tag',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tag',
            field=models.ManyToManyField(blank=True, to='urlmodel.Tag'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
