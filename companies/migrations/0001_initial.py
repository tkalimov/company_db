# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=255)),
                ('investors', models.TextField()),
                ('last_funding_amount', models.IntegerField()),
                ('cached_mobile_mattermark', models.IntegerField()),
                ('employees_6_months_ago', models.IntegerField()),
                ('keywords', models.CharField(max_length=255)),
                ('uniques_wow', models.IntegerField()),
                ('pre_money_valuation', models.IntegerField()),
                ('last_funding_date', models.DateField()),
                ('alert_hash', models.IntegerField()),
                ('mobile_downloads_mom', models.IntegerField()),
                ('continent', models.CharField(max_length=255)),
                ('cached_uniques_month_ago', models.IntegerField()),
                ('industries', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('employees_12_months_growth', models.IntegerField()),
                ('employees_mom', models.IntegerField()),
                ('employees_added_since_last_funding', models.IntegerField()),
                ('months_since_last_funding', models.IntegerField()),
                ('cached_mobile_downloads', models.IntegerField()),
                ('state', models.CharField(max_length=255)),
                ('interested', models.IntegerField()),
                ('company_name', models.CharField(max_length=255)),
                ('is_raising', models.CharField(max_length=255)),
                ('new_person_months_since_last_funding', models.IntegerField()),
                ('employees_month_ago', models.IntegerField()),
                ('est_founding_date', models.DateField()),
                ('employees_added_in_month', models.IntegerField()),
                ('mattermark_score', models.IntegerField()),
                ('cached_uniques', models.IntegerField()),
                ('cached_mobile_downloads_week_ago', models.IntegerField()),
                ('employees_6_months_growth', models.IntegerField()),
                ('custom_score', models.IntegerField()),
                ('cached_mobile_downloads_month_ago', models.IntegerField()),
                ('total_funding', models.TextField()),
                ('employees_12_months_ago', models.IntegerField()),
                ('momentum_score', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
                ('new_funding_employee_growth', models.IntegerField()),
                ('employees_added_in_6_months', models.IntegerField()),
                ('stage', models.CharField(max_length=255)),
                ('business_models', models.CharField(max_length=255)),
                ('user_tags', models.IntegerField()),
                ('has_mobile', models.CharField(max_length=255)),
                ('mobile_downloads_wow', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('raised_amount', models.IntegerField()),
                ('cached_growth_score', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('cached_uniques_week_ago', models.IntegerField()),
                ('raising_amount', models.IntegerField()),
                ('employees', models.IntegerField()),
                ('uniques_mom', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
