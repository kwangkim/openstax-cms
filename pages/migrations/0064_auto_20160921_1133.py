# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0063_ap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='give',
            name='payment_method_4_content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='give',
            name='payment_method_4_heading',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='institutions',
            name='logo',
            field=models.ForeignKey(blank=True, help_text='Image should be 340px wide, horizontal images are ideal', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
