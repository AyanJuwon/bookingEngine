# Generated by Django 3.2 on 2022-02-11 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_rename_booked_space_bookedlisting_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedlisting',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing'),
        ),
    ]
