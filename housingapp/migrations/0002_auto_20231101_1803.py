# Generated by Django 2.1.15 on 2023-11-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='county',
        ),
        migrations.DeleteModel(
            name='County',
        ),
    ]
