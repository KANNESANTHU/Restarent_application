# Generated by Django 3.0.6 on 2020-05-28 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'reservation', 'verbose_name_plural': 'reservations'},
        ),
    ]