from .models import CarMake, CarModel

def initiate():
    # only seed once
    if CarMake.objects.exists() or CarModel.objects.exists():
        return

    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    make_instances = [CarMake.objects.create(**d) for d in car_make_data]

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV",   "year": 2023, "car_make": make_instances[0], "dealer_id": 3},
        {"name": "Qashqai",    "type": "SUV",   "year": 2023, "car_make": make_instances[0], "dealer_id": 3},
        {"name": "XTRAIL",     "type": "SUV",   "year": 2023, "car_make": make_instances[0], "dealer_id": 3},

        {"name": "A-Class",    "type": "SUV",   "year": 2023, "car_make": make_instances[1], "dealer_id": 29},
        {"name": "C-Class",    "type": "SUV",   "year": 2023, "car_make": make_instances[1], "dealer_id": 29},
        {"name": "E-Class",    "type": "SUV",   "year": 2023, "car_make": make_instances[1], "dealer_id": 29},

        {"name": "A6",         "type": "SUV",   "year": 2023, "car_make": make_instances[2], "dealer_id": 1},
        {"name": "Q5",         "type": "SUV",   "year": 2023, "car_make": make_instances[2], "dealer_id": 1},
        {"name": "Q7",         "type": "SUV",   "year": 2023, "car_make": make_instances[2], "dealer_id": 1},

        {"name": "Sorento",    "type": "SUV",   "year": 2023, "car_make": make_instances[3], "dealer_id": 2},
        {"name": "Carnival",   "type": "SUV",   "year": 2023, "car_make": make_instances[3], "dealer_id": 2},
        {"name": "Cerato",     "type": "Sedan", "year": 2023, "car_make": make_instances[3], "dealer_id": 2},

        {"name": "Corolla",    "type": "Sedan", "year": 2023, "car_make": make_instances[4], "dealer_id": 3},
        {"name": "Camry",      "type": "Sedan", "year": 2023, "car_make": make_instances[4], "dealer_id": 3},
        {"name": "Kluger",     "type": "SUV",   "year": 2023, "car_make": make_instances[4], "dealer_id": 3},
    ]

    for row in car_model_data:
        CarModel.objects.create(**row)
