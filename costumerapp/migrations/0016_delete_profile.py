# Generated by Django 5.0.7 on 2024-07-25 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0015_remove_profile_first_name_remove_profile_last_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
