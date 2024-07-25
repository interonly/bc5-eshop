from django.db import models
from django.contrib.auth.models import User


class Costumer(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    age = models.IntegerField(verbose_name="Возраст", null=True, blank=True)
    gender = models.CharField(verbose_name="Пол", max_length=50)
    user = models.OneToOneField(
        to=User,
        verbose_name="Логин",
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return self.name