# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150211_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='last_funding_amount',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
    ]
