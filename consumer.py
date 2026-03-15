from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "library",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: m.decode("utf-8")
)

def validate(data):
    required_fields = ["user", "book", "action", "time"]

    for field in required_fields:
        if field not in data:
            return False

    if data["action"] not in ["borrow", "return"]:
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

    except:
        print("NOT VALID:", msg)
