# vehicles/populate.py
from .models import CarMake, CarModel

def initiate():
    if CarMake.objects.exists():
        return  # already seeded

    makes = [
        {"name": "NISSAN",  "description": "Great cars. Japanese technology"},
        {"name": "Mercedes","description": "Great cars. German technology"},
        {"name": "Audi",    "description": "Great cars. German technology"},
        {"name": "Kia",     "description": "Great cars. Korean technology"},
        {"name": "Toyota",  "description": "Great cars. Japanese technology"},
    ]
    make_objs = [CarMake.objects.create(**m) for m in makes]

    models = [
        {"name":"Pathfinder","type":"SUV","year":2023,"car_make":make_objs[0],"dealer_id":1},
        {"name":"Qashqai",  "type":"SUV","year":2023,"car_make":make_objs[0],"dealer_id":1},
        {"name":"XTRAIL",   "type":"SUV","year":2023,"car_make":make_objs[0],"dealer_id":1},

        {"name":"A-Class",  "type":"Sedan","year":2023,"car_make":make_objs[1],"dealer_id":2},
        {"name":"E-Class",  "type":"Sedan","year":2023,"car_make":make_objs[1],"dealer_id":2},
        {"name":"C-Class",  "type":"Sedan","year":2023,"car_make":make_objs[1],"dealer_id":2},

        {"name":"A6",       "type":"Sedan","year":2023,"car_make":make_objs[2],"dealer_id":3},
        {"name":"Q7",       "type":"SUV",  "year":2023,"car_make":make_objs[2],"dealer_id":3},
        {"name":"A5",       "type":"Coupe","year":2023,"car_make":make_objs[2],"dealer_id":3},

        {"name":"Sorento",  "type":"SUV","year":2023,"car_make":make_objs[3],"dealer_id":4},
        {"name":"Carnival", "type":"SUV","year":2023,"car_make":make_objs[3],"dealer_id":4},
        {"name":"Cerato",   "type":"Sedan","year":2023,"car_make":make_objs[3],"dealer_id":4},

        {"name":"Corolla",  "type":"Sedan","year":2023,"car_make":make_objs[4],"dealer_id":5},
        {"name":"Camry",    "type":"Sedan","year":2023,"car_make":make_objs[4],"dealer_id":5},
        {"name":"Kluger",   "type":"SUV","year":2023,"car_make":make_objs[4],"dealer_id":5},
    ]
    CarModel.objects.bulk_create(CarModel(**m) for m in models)
