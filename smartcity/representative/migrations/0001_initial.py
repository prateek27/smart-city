# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=200)),
                ('project_date', models.DateTimeField(default=datetime.datetime(2015, 10, 31, 5, 58, 3, 803803, tzinfo=utc))),
                ('project_deadline', models.DateTimeField(default=datetime.datetime(2015, 10, 31, 5, 58, 3, 803836, tzinfo=utc))),
                ('current_spent', models.IntegerField(default=0)),
                ('total_spent', models.CharField(max_length=200)),
                ('started_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
