# Generated by Django 5.0.6 on 2024-07-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_view_new_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='photo_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на фото'),
        ),
    ]
