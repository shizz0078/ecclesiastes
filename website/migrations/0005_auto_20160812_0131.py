# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-12 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160812_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date_modified',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
