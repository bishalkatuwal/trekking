# Generated by Django 5.1.3 on 2024-11-20 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0006_remove_tripcategory_trip_trip_trip_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='trek.tripcategory'),
            preserve_default=False,
        ),
    ]
