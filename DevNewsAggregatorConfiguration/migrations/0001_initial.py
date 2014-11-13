# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlContent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('url', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('scraping_strategy', models.IntegerField()),
                ('outer_content_selector', models.TextField()),
                ('inner_content_selector', models.TextField()),
                ('title_selector', models.TextField()),
                ('ignore_first_n_posts', models.IntegerField(default=0)),
                ('ignore_last_n_posts', models.IntegerField(default=0)),
                ('date_parsing_strategy', models.IntegerField()),
                ('date_selector', models.TextField()),
                ('time_selector', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
