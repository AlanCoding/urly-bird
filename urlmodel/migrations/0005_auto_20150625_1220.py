# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlmodel', '0004_auto_20150624_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='posted_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='clicked_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
