# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_authors_senior_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='senior_author',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]