# Generated by Django 3.2.25 on 2024-11-18 08:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0004_page_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childpage',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
