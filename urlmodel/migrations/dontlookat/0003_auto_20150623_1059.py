# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('urlmodel', '0002_auto_20150621_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='URL',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.CharField(blank=True, default=datetime.datetime(2015, 6, 23, 14, 59, 27, 250666, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(blank=True, default='default title', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookmarker',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
