# Generated by Django 5.0.7 on 2024-07-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_created_at_product_expiration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='фото'),
        ),
    ]