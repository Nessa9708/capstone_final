# vehicles/views.py
from django.http import JsonResponse
from .models import CarMake, CarModel
from .populate import initiate   # <-- add this

def get_cars(request):
    if not CarMake.objects.exists():
        initiate()  # seed once

    cars = []
    for cm in CarModel.objects.select_related("car_make").all():
        cars.append({
            "CarModel": cm.name,
            "CarMake": cm.car_make.name,
            "type": cm.type,
            "year": cm.year,
            "dealer_id": cm.dealer_id,
        })
    return JsonResponse({"CarModels": cars})
