# Generated by Django 5.0.7 on 2024-07-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='views_qty',
            field=models.IntegerField(default=0, verbose_name='Общее кол-во просмотров'),
        ),
    ]
