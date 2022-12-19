from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    short_disc = models.TextField(max_length=170)
    full_disc = models.TextField(max_length=255)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
