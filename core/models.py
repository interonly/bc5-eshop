from django.db import models
from costumerapp.models import Costumer


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
    costumer_views = models.ManyToManyField(
        to=Costumer,
        verbose_name="Просмотры пользователей", 
        default=0
    )
    views_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.name
