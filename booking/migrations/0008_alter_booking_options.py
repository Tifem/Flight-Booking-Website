# Generated by Django 4.0.5 on 2022-07-09 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_rename_passenger_booking_passengers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['flight__departure_datetime']},
        ),
    ]
