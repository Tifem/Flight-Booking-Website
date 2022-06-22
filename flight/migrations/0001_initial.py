# Generated by Django 4.0.5 on 2022-06-21 22:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeroplane', models.CharField(max_length=200)),
                ('departure_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('arrival_datetime', models.DateTimeField(auto_now=True)),
                ('max_passengers', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_departure', to='airport.airport')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_destination', to='airport.airport')),
            ],
        ),
    ]
