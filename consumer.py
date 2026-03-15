from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "carsharing",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),  # ИСПРАВЛЕНО
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def validate(data):
    required_fields = ["user", "car", "action", "time"]
    for field in required_fields:
        if field not in data:
            return False
    if data["action"] not in ["start_ride", "end_ride"]:
        return False
    return True

for message in consumer:
    data = message.value  # Теперь data - это словарь!
    if validate(data):
        print("VALID:", data)
    else:
        print("NOT VALID:", data)
