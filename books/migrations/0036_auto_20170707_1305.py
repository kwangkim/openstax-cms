# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0035_auto_20170706_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ibook_volume_2_isbn_10',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='ibook_volume_2_isbn_13',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
