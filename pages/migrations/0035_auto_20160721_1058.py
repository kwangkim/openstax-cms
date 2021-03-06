# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 15:58
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_auto_20160721_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='row_1',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='arrow-left', label='Left column content')), ('center_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='up-left', label='Center column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='arrow-right', label='Right column content'))))),), blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='arrow-left', label='Left column content')), ('center_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='up-left', label='Center column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('cta', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), icon='arrow-right', label='Right column content'))))),), blank=True),
        ),
    ]
