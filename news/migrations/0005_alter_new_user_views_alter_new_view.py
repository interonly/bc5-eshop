# Generated by Django 5.0.6 on 2024-07-11 07:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_newcategory_newscategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='user_views',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Уникальные просмотры пользователей'),
        ),
        migrations.AlterField(
            model_name='new',
            name='view',
            field=models.IntegerField(verbose_name='Общее кол-во просмотров'),
        ),
    ]
