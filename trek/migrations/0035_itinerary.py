# Generated by Django 5.1.3 on 2024-12-23 07:37

import django.db.models.deletion
import froala_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0034_rename_add_date_addtocart_added_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('day_no', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
                ('trek_duration', models.PositiveIntegerField()),
                ('highest_altitude', models.PositiveIntegerField()),
                ('flight_hours', models.PositiveIntegerField()),
                ('summary', froala_editor.fields.FroalaField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary', to='trek.trip')),
            ],
            options={
                'ordering': ['day_no'],
            },
        ),
    ]
