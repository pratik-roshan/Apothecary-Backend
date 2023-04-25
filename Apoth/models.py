from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=1000)
    sname = models.CharField(max_length=1000)
    property = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    photo= models.ImageField(blank=bool)
