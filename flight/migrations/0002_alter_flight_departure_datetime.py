# Generated by Django 4.0.5 on 2022-06-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='departure_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]