# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='business_models',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='continent',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='domain',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='has_mobile',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='industries',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='is_raising',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='keywords',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='region',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='stage',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
