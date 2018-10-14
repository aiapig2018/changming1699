# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-04 13:20
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourstory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='ourstory/%Y/%m/%d', verbose_name='故事背景图'),
        ),
        migrations.AddField(
            model_name='article',
            name='storycontent',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='详情介绍'),
        ),
    ]
