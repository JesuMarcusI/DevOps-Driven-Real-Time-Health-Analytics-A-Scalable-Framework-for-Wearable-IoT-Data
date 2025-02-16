from kafka import KafkaProducer
import json
import time
import random

KAFKA_BROKER = "kafka-service:9092"
TOPIC = "health-monitoring"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    return {
        "device_id": random.randint(1000, 9999),
        "heart_rate": random.randint(60, 120),
        "temperature": round(random.uniform(36.0, 38.5), 1),
        "oxygen_level": random.randint(90, 100)
    }

while True:
    data = generate_data()
    producer.send(TOPIC, value=data)
    print(f"Sent: {data}")
    time.sleep(5)
