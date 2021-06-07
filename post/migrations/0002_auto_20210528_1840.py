# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-05-28 10:40
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cname',
            field=models.CharField(max_length=30, unique=True, verbose_name='类别名称'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_created=True, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=80, unique=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tname',
            field=models.CharField(max_length=30, unique=True, verbose_name='标签名称'),
        ),
    ]