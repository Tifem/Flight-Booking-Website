# Generated by Django 4.0.5 on 2022-06-29 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_booking_passenger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='passenger',
            new_name='passengers',
        ),
    ]
