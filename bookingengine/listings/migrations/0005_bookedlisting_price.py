# Generated by Django 3.2 on 2022-02-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_bookedlisting_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedlisting',
            name='price',
            field=models.DecimalField(decimal_places=2, default=40, max_digits=6),
            preserve_default=False,
        ),
    ]