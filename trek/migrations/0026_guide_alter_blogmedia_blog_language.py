# Generated by Django 5.1.3 on 2024-12-11 07:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0025_remove_blog_blog_media_blogmedia_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='guide/photo')),
                ('bio', models.TextField(blank=True, null=True)),
                ('experience_years', models.PositiveIntegerField(default=1)),
                ('language_spoken', models.CharField(max_length=100)),
                ('available_from', models.DateField(default=django.utils.timezone.now)),
                ('available_to', models.DateField(default=django.utils.timezone.now)),
                ('daily_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('hourly_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='blogmedia',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_media', to='trek.blog'),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trek.guide')),
            ],
        ),
    ]
