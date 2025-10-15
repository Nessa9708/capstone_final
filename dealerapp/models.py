from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    class CarType(models.TextChoices):
        SEDAN = "Sedan", "Sedan"
        SUV   = "SUV", "SUV"
        WAGON = "Wagon", "Wagon"
        COUPE = "Coupe", "Coupe"
        HATCH = "Hatchback", "Hatchback"

    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    dealer_id = models.IntegerField()                     # integer id from Cloudant/Dealership DB later
    type = models.CharField(max_length=20, choices=CarType.choices)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
