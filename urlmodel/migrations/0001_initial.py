# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('URL', models.CharField(max_length=300)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('posted_at', models.DateTimeField()),
                ('title', models.CharField(null=True, max_length=255)),
                ('description', models.CharField(null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('clicked_at', models.DateTimeField(null=True)),
                ('bookmark', models.ForeignKey(to='urlmodel.Bookmark')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tag',
            field=models.ForeignKey(to='urlmodel.Tag'),
        ),
    ]
