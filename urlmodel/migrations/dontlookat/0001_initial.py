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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('URL', models.URLField(max_length=300)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('posted_at', models.DateTimeField()),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmarker',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(default='M', choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('clicked_at', models.DateTimeField(null=True)),
                ('bookmark', models.ForeignKey(to='urlmodel.Bookmark')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tag',
            field=models.ManyToManyField(to='urlmodel.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
