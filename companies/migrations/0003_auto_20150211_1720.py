# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150211_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='est_founding_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='last_funding_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
