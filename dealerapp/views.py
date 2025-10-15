from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .populate import initiate
from django.http import JsonResponse

def login_user(request):
    if request.method == "GET":
        return render(request, "login.html")
    user = authenticate(request,
                        username=request.POST.get("username"),
                        password=request.POST.get("password"))
    if user:
        login(request, user)
        return redirect("home")
    return render(request, "login.html", {"error": "Invalid credentials"})

def logout_user(request):
    uname = request.user.username if request.user.is_authenticated else ""
    logout(request)
    return HttpResponse(f"""
        <html><body>
        <script>alert("Logging out {uname}..."); window.location="/";</script>
        </body></html>
    """)

@csrf_exempt
def register_user(request):
    if request.method == "GET":
        return render(request, "register.html")
    username = request.POST.get("username")
    if User.objects.filter(username=username).exists():
        return render(request, "register.html", {"error": "User already exists"})
    user = User.objects.create_user(
        username=username,
        password=request.POST.get("password"),
        email=request.POST.get("email",""),
        first_name=request.POST.get("first_name",""),
        last_name=request.POST.get("last_name",""),
    )
    login(request, user)
    return redirect("home")

def spa(request):
    # render Vite-built React app
    return render(request, "index.html")

def logout_alert(request):
    uname = request.GET.get("u", "")
    return HttpResponse(f"""
      <html><body>
      <script>
        alert("Logging out {uname}...");
        window.location = "/";
      </script>
      </body></html>
    """)

def get_cars(request):
    # Seed data on first call if empty (helps match IBM lab flow)
    if CarMake.objects.count() == 0 and CarModel.objects.count() == 0:
        initiate()

    # Build the payload
    car_models = CarModel.objects.select_related("car_make").order_by("car_make__name", "name", "year")
    cars = []
    for cm in car_models:
        cars.append({
            "CarModel": cm.name,
            "CarMake": cm.car_make.name,
            "type": cm.type,
            "year": cm.year,
            "dealerId": cm.dealer_id,
        })
    return JsonResponse({"CarModels": cars})