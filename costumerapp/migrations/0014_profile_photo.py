# Generated by Django 5.0.7 on 2024-07-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0013_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='фото'),
        ),
    ]
