# Generated by Django 2.1.15 on 2023-12-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0006_auto_20231208_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseadvertisement',
            name='rent_per_month',
            field=models.PositiveIntegerField(default=1000),
            preserve_default=False,
        ),
    ]
