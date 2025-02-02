# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-07 00:44
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0036_auto_20161006_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertystate',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orgs.Organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taxlotstate',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orgs.Organization'),
            preserve_default=False,
        ),
    ]
