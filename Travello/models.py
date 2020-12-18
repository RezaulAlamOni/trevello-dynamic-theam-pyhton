from django.db import models


# Create your models here.

class Destination(models.Model):
    mame = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picss')
    desc = models.TextField()
    places = models.TextField()
    price = models.IntegerField()
