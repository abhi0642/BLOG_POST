# Generated by Django 3.2.8 on 2021-11-04 01:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_auto_20211104_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 1, 14, 37, 122415, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 1, 14, 37, 122073, tzinfo=utc)),
        ),
    ]