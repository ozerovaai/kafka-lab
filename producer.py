from kafka import KafkaProducer
from generator import generate_carsharing_event
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: v.encode("utf-8")
)

topic = "carsharing"

while True:
    message = generate_carsharing_event()
    print("Produced:", message)
    producer.send(topic, message)
    time.sleep(2)  # генерация каждые 2 секунды
