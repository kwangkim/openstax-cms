# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0005_errata_supporting_documentation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='errata',
            name='supporting_documentation',
        ),
    ]
