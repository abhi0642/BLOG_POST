# Generated by Django 3.2.8 on 2021-11-02 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20211102_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 18, 47, 0, 231231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 18, 47, 0, 230898, tzinfo=utc)),
        ),
    ]
