# Generated by Django 3.2.7 on 2021-10-06 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_ecom', '0003_delete_countorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='timestamp',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
