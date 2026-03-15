import random
import json
from datetime import datetime

books = [
    "War and Peace",
    "Crime and Punishment",
    "The Hobbit",
    "1984",
    "The Master and Margarita"
]

users = ["Ivan", "Anna", "Sergey", "Maria", "Alex"]

actions = ["borrow", "return"]

def generate_library_event():
    data = {
        "user": random.choice(users),
        "book": random.choice(books),
        "action": random.choice(actions),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return json.dumps(data)
