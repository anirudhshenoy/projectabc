# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0005_chapterdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chapterDetails',
            new_name='chapterDetail',
        ),
    ]