# Generated by Django 2.2.3 on 2019-07-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0007_auto_20190723_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
