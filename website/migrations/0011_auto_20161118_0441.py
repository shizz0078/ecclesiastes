# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_contactstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactstatus',
            name='contact_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.ContactUs'),
        ),
    ]
