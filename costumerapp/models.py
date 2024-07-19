from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
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
        

class Profile(models.Model):
    first_name = models.OneToOneField(
        to=Costumer,
        verbose_name="Имя",
        max_length=50,
        null = False, blank=False,
        on_delete=models.DO_NOTHING
        )
    last_name = models.CharField(verbose_name="Фамилия", max_length=50, null=False, blank=False)
    bio = models.TextField(verbose_name="Био", null=True, blank=True)
    social_link = models.URLField(verbose_name="соц.сети", max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(help_text='Контактный номер телефона', verbose_name="Номер телефона", region="KG", max_length=35, null=True, blank=True)
