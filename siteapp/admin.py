from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CarMake, CarModel

admin.site.register(CarMake)
admin.site.register(CarModel)
