# Generated by Django 5.0.6 on 2024-07-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0008_rename_user_profile_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]
