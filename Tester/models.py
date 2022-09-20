from django.db import models
# Create your models here.
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Consumer(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='Vendor_detail')
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.vendor)