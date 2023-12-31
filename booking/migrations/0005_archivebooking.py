# Generated by Django 3.2.23 on 2023-11-25 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_is_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archive_booking', to='booking.booking')),
            ],
        ),
    ]
