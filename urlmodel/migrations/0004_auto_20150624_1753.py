# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlmodel', '0003_auto_20150623_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='posted_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='bookmarker',
            name='age',
            field=models.IntegerField(null=True, default=22),
        ),
    ]
