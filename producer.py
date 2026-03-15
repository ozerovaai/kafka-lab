from kafka import KafkaProducer
from generator import generate_library_event
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: v.encode("utf-8")
)

topic = "library"

while True:
    message = generate_library_event()

    print("Produced:", message)

    producer.send(topic, message)

    time.sleep(3)
