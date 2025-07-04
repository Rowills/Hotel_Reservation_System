# Generated by Django 5.1.4 on 2025-01-06 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guest_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')], max_length=20)),
                ('capacity', models.IntegerField()),
                ('price_per_night', models.FloatField()),
                ('amenities', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_price', models.FloatField()),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Refunded', 'Refunded')], max_length=10)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
    ]
