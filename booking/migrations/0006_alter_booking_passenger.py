# Generated by Django 4.0.5 on 2022-06-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='passenger',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='booking.passenger'),
        ),
    ]
