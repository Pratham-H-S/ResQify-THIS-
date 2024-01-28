# Generated by Django 4.2.7 on 2024-01-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=1000, null=True)),
                ('no_of_bookings', models.CharField(blank=True, max_length=5000, null=True)),
                ('rating', models.CharField(blank=True, max_length=200, null=True)),
                ('cust_name', models.CharField(blank=True, max_length=500, null=True)),
                ('cust_username', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
    ]