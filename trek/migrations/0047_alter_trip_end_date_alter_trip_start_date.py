# Generated by Django 5.1.3 on 2025-01-26 09:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0046_alter_trips_review_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
