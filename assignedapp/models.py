from django.db import models
class register(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Country = models.CharField(max_length=100)


# Create your models here.
