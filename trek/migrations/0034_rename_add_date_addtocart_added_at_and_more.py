# Generated by Django 5.1.3 on 2024-12-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0033_addtocart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='add_date',
            new_name='added_at',
        ),
        migrations.AlterUniqueTogether(
            name='addtocart',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]