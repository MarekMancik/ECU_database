# Generated by Django 5.0.4 on 2024-05-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_ecu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecu',
            name='al_part_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
