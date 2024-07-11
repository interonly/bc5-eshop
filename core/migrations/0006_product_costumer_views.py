# Generated by Django 5.0.6 on 2024-07-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_description_alter_product_name_and_more'),
        ('costumerapp', '0003_profile_alter_costumer_age_alter_costumer_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='costumer_views',
            field=models.ManyToManyField(default=0, to='costumerapp.costumer', verbose_name='Кол-во просмотров'),
        ),
    ]
