# Generated by Django 5.1.3 on 2024-11-21 06:50

import django.db.models.deletion
import django.utils.timezone
import froala_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0009_trip_slug_alter_tripcategory_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='image',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='available_seats',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='price',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='tripcategory',
            name='trip',
        ),
        migrations.AddField(
            model_name='trip',
            name='available_seats',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='description',
            field=froala_editor.fields.FroalaField(default='Default description text'),
        ),
        migrations.AddField(
            model_name='trip',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='trek.destination'),
        ),
        migrations.AddField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trip',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='trek.tripcategory'),
        ),
        migrations.AddField(
            model_name='tripcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trip_pics'),
        ),
        migrations.AddField(
            model_name='tripcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tripcategory',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tripcategory',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
