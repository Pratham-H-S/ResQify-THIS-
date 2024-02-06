# Generated by Django 4.2.7 on 2024-02-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mechanic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mech_Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mech_username', models.CharField(blank=True, max_length=500, null=True)),
                ('cust_username', models.CharField(blank=True, max_length=500, null=True)),
                ('booking_date', models.CharField(blank=True, max_length=200, null=True)),
                ('booking_time', models.CharField(blank=True, max_length=200, null=True)),
                ('issue_desc', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'mech_Bookings',
            },
        ),
    ]
