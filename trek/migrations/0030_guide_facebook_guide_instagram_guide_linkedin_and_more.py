# Generated by Django 5.1.3 on 2024-12-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0029_alter_language_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='instagram',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='linkedin',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='twitter',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='whatsapp',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
