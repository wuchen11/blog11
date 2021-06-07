# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-05-25 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=80, unique=True)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Category')),
            ],
            options={
                'db_table': 't_Post',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_tag',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='post.Tag'),
        ),
    ]