# Generated by Django 4.0.5 on 2022-06-26 08:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_alter_flight_departure_alter_flight_destination'),
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
