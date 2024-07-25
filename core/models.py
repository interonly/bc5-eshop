from django.db import models
from costumerapp.models import Costumer
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    price = models.IntegerField(verbose_name="Цена")
    qty = models.IntegerField(verbose_name="Кол-во", default=0)
    category = models.ForeignKey(
        to=ProductCategory,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    image = models.ImageField(
        verbose_name="фото",
        upload_to="products/",
        null=True, blank=True,
    )
    rating = models.IntegerField(default=0)
    guarantee = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    costumer_views = models.ManyToManyField(
        to=Costumer,
        verbose_name="Просмотры пользователей", 
        default=0
    )
    views_qty = models.IntegerField(verbose_name="Общее кол-во просмотров" ,default=0)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    bio = models.TextField(null=True, blank=True)
    social_link = models.CharField(max_length=100)
    phone_number = PhoneNumberField(help_text='Контактный номер телефона', verbose_name="Номер телефона", region="KG", max_length=35, null=True, blank=True)
    photo = models.ImageField(
        verbose_name="фото",
        upload_to="profiles/",
        null=True, blank=True
    )