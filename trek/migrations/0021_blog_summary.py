# Generated by Django 5.1.3 on 2024-12-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0020_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]