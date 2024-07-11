# Generated by Django 5.0.6 on 2024-07-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0004_alter_profile_bio_alter_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='соц.сети'),
        ),
    ]
