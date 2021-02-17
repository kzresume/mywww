# Generated by Django 3.1.4 on 2021-02-13 18:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
    ]