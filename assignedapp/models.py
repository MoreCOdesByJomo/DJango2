from django.db import models
class Register(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)


# Create your models here.
