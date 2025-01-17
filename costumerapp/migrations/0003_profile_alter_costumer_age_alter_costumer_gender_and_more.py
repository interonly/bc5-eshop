# Generated by Django 5.0.6 on 2024-07-11 07:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0002_costumer_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('bio', models.TextField(blank=True, null=True)),
                ('social_link', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='costumer',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='gender',
            field=models.CharField(max_length=50, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
    ]
