# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:55
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0078_auto_20170110_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='faq_link',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='intro_paragraph',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]