# Generated by Django 5.1.3 on 2024-12-11 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0026_guide_alter_blogmedia_blog_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='guide',
        ),
        migrations.AlterField(
            model_name='guide',
            name='language_spoken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trek.language'),
        ),
    ]
