# Generated by Django 5.0.4 on 2024-05-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_ecu', '0004_alter_ecu_testing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecu',
            name='ecu_comment',
            field=models.TextField(max_length=30),
        ),
    ]
