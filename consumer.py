from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "carsharing",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: m.decode("utf-8")
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
    msg = message.value
    try:
        data = json.loads(msg)
        if validate(data):
            print("VALID:", data)
        else:
            print("NOT VALID:", msg)
    except Exception:
        print("NOT VALID:", msg)
