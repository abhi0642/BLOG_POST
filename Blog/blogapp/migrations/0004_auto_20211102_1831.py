# Generated by Django 3.2.8 on 2021-11-02 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20211102_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 18, 31, 32, 770497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 18, 31, 32, 770173, tzinfo=utc)),
        ),
    ]
