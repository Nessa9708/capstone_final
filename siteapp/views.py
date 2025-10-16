from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import CarMake, CarModel

# Optional: auto-populate on first call
try:
    from .populate import initiate
except Exception:
    initiate = None

def get_cars(request):
    if CarMake.objects.count() == 0 and initiate:
        initiate()

    cars = []
    for cm in CarModel.objects.select_related("car_make").all():
        cars.append({
            "CarModel": cm.name,
            "CarMake": cm.car_make.name,
            "type": cm.type,
            "year": cm.year,
        })
    return JsonResponse({"CarModels": cars})
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')