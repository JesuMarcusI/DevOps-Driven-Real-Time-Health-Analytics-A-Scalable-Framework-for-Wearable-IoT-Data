from kafka import KafkaConsumer
import json

KAFKA_BROKER = "kafka-service:9092"
TOPIC = "health-monitoring"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def process_data(record):
    if record["heart_rate"] > 100 or record["oxygen_level"] < 92:
        print(f" ALERT! High Risk Detected: {record}")

for msg in consumer:
    process_data(msg.value)
