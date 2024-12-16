# Generated by Django 5.1.3 on 2024-12-10 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0021_blog_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/images')),
                ('vedio', models.FileField(blank=True, null=True, upload_to='blog/video')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='trek.blog')),
            ],
        ),
        migrations.DeleteModel(
            name='AboutUs',
        ),
    ]