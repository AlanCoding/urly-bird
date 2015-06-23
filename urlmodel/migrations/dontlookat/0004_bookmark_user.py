# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urlmodel', '0003_auto_20150623_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=False,
        ),
    ]
