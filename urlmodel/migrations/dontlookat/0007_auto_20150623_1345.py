# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('urlmodel', '0006_auto_20150623_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
