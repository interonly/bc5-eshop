# Generated by Django 5.0.6 on 2024-07-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0006_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
    ]
