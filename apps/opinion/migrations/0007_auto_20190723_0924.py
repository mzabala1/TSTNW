# Generated by Django 2.2.3 on 2019-07-23 09:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0006_auto_20190723_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='datetime',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 9, 24, 3, 774393, tzinfo=utc)),
        ),
    ]
