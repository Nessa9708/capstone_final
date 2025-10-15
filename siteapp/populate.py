from .models import CarMake, CarModel

def initiate():
    # 5 makes
    makes_raw = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]
    make_objs = [CarMake.objects.create(**m) for m in makes_raw]

    # 15 models (3 per make)
    models_raw = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": make_objs[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": make_objs[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": make_objs[0]},
        {"name": "A-Class", "type": "SEDAN", "year": 2023, "car_make": make_objs[1]},
        {"name": "E-Class", "type": "SEDAN", "year": 2023, "car_make": make_objs[1]},
        {"name": "GLA", "type": "SUV", "year": 2023, "car_make": make_objs[1]},
        {"name": "A6", "type": "SEDAN", "year": 2023, "car_make": make_objs[2]},
        {"name": "Q5", "type": "SUV", "year": 2023, "car_make": make_objs[2]},
        {"name": "Q7", "type": "SUV", "year": 2023, "car_make": make_objs[2]},
        {"name": "Sorento", "type": "SUV", "year": 2023, "car_make": make_objs[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": make_objs[3]},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "car_make": make_objs[3]},
        {"name": "Corolla", "type": "SEDAN", "year": 2023, "car_make": make_objs[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "car_make": make_objs[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": make_objs[4]},
    ]
    for m in models_raw:
        CarModel.objects.create(**m)
