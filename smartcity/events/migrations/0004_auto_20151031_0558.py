# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151030_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 5, 58, 3, 801241, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
