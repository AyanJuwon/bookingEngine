# Generated by Django 3.2 on 2022-02-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_rename_listing_bookedlisting_booking_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinginfo',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
