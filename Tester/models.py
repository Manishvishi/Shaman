from django.db import models

# Create your models here.
class vendor(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name, self.city

class consumer(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    product = models.CharField(max_length=30)

    def __str__(self):
        return self.name, self.city, self.product
