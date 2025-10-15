from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    TYPE_CHOICES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    dealer_id = models.IntegerField(default=0)        # maps to dealer in Mongo (later modules)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.IntegerField(default=2023)

    def __str__(self):
        return self.name
