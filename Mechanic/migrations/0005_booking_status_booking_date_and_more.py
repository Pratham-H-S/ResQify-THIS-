# Generated by Django 4.2.7 on 2024-01-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mechanic', '0004_booking_status_duration_kilometers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_status',
            name='booking_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking_status',
            name='booking_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
