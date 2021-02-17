# Generated by Django 3.1.4 on 2021-02-16 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0014_auto_20210212_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('done', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterField(
            model_name='holiday_request',
            name='date_begin',
            field=models.DateField(default=datetime.date(2021, 2, 16)),
        ),
        migrations.AlterField(
            model_name='holiday_request',
            name='date_end',
            field=models.DateField(default=datetime.date(2021, 2, 16)),
        ),
    ]
