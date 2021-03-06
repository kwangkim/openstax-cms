# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160222_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyresources',
            name='link_text',
            field=models.CharField(default='', help_text='Call to Action Text', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentresources',
            name='link_text',
            field=models.CharField(default='', help_text='Call to Action Text', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]
