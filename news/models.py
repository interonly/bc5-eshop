from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    view = models.IntegerField()