# Generated by Django 5.0.6 on 2024-07-19 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0007_alter_costumer_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='first_name',
        ),
    ]
