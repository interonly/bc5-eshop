# Generated by Django 5.0.6 on 2024-07-11 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newcategory_alter_new_article_alter_new_title_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewCategory',
            new_name='NewsCategory',
        ),
    ]
