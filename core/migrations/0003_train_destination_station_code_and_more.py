# Generated by Django 5.1 on 2024-08-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_station_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='destination_station_code',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='source_station_code',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
