# Generated by Django 3.1.4 on 2021-02-21 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0020_info_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday_request',
            name='date_begin',
            field=models.DateField(default=datetime.date(2021, 2, 21)),
        ),
        migrations.AlterField(
            model_name='holiday_request',
            name='date_end',
            field=models.DateField(default=datetime.date(2021, 2, 21)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
