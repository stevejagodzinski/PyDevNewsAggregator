# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DevNewsAggregatorConfiguration', '0003_auto_20141128_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlcontent',
            name='name',
            field=models.CharField(max_length=30, unique=True),
            preserve_default=True,
        ),
    ]
