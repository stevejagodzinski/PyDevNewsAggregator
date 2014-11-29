# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DevNewsAggregatorConfiguration', '0002_auto_20141126_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlcontent',
            name='date_parsing_strategy',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='htmlcontent',
            name='enabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='htmlcontent',
            name='time_selector',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
