# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DevNewsAggregatorConfiguration', '0005_auto_20141129_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlcontent',
            name='date_selector',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='htmlcontent',
            name='inner_content_selector',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='htmlcontent',
            name='outer_content_selector',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='htmlcontent',
            name='title_selector',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
