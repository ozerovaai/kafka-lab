import random
import json
from datetime import datetime

users = ["Ivan", "Anna", "Sergey", "Maria", "Alex"]
cars = ["Tesla Model 3", "BMW i3", "Audi e-tron", "Volkswagen ID.4", "Nissan Leaf"]
actions = ["start_ride", "end_ride"]

def generate_carsharing_event():
    data = {
        "user": random.choice(users),
        "car": random.choice(cars),
        "action": random.choice(actions),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return json.dumps(data)
