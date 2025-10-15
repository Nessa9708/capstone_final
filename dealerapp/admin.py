from django.contrib import admin
from .models import CarMake, CarModel

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "car_make", "type", "year", "dealer_id")
    list_filter = ("car_make", "type", "year")
    search_fields = ("name",)
