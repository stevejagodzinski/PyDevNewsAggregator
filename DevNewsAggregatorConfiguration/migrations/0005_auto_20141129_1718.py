# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DevNewsAggregatorConfiguration', '0004_auto_20141129_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlcontent',
            name='time_selector',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
