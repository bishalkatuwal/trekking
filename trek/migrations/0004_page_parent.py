# Generated by Django 3.2.25 on 2024-11-18 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0003_auto_20241117_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='trek.page'),
        ),
    ]
