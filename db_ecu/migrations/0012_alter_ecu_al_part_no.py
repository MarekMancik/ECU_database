# Generated by Django 5.0.4 on 2024-07-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_ecu', '0011_alter_ecu_al_part_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecu',
            name='al_part_no',
            field=models.CharField(blank=True, default='N/A', max_length=11, null=True),
        ),
    ]
