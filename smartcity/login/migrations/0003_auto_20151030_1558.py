# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_auto_20151030_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_image', models.ImageField(default=b'profile_image/default1.jpg', upload_to=b'profile_image/', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_handle',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_city',
            field=models.CharField(default=b'Chandigarh', max_length=20, choices=[(b'Chandigarh', b'Chandigarh'), (b'Jalandhar', b'Jalandhar'), (b'Amritsar', b'Amritsar'), (b'Ludhiana', b'Ludhiana')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default=b'profile_image/default1.jpg', upload_to=b'profile_image/', blank=True),
            preserve_default=True,
        ),
    ]
