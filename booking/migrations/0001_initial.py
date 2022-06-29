# Generated by Django 4.0.5 on 2022-06-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.PositiveIntegerField(blank=True, null=True)),
                ('passenger_first_name', models.CharField(max_length=100)),
                ('passenger_last_name', models.CharField(max_length=100)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_flight', to='flight.flight')),
            ],
            options={
                'ordering': ['reference_no'],
            },
        ),
    ]
