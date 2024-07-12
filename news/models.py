from django.db import models
from django.contrib.auth.models import User

class NewsCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    article = models.TextField(verbose_name="Содержание")
    category = models.ForeignKey(
        to=NewsCategory,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    views = models.IntegerField(verbose_name="Общее кол-во просмотров")
    user_views = models.ManyToManyField(
        to=User,
        verbose_name="Уникальные просмотры пользователей",
        blank=True,
    )

    def __str__(self):
        return self.title