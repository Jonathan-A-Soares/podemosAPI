# Generated by Django 3.0.4 on 2020-04-17 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200416_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
