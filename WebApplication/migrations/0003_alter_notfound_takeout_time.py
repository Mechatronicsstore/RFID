# Generated by Django 3.2.7 on 2021-12-09 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0002_auto_20211130_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notfound',
            name='takeout_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 9, 1, 23, 31, 622515)),
        ),
    ]