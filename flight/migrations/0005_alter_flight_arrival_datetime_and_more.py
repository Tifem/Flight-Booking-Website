# Generated by Django 4.0.5 on 2022-06-27 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_alter_flight_arrival_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
