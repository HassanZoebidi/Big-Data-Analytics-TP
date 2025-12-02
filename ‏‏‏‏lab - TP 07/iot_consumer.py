# iot_consumer.py
# Simple Kafka consumer that reads messages from topic 'tp-iot' and prints them.
# Usage:
#   pip install kafka-python
#   python iot_consumer.py

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'tp-iot',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    consumer_timeout_ms=20000,  # exit after 20s of inactivity
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Listening for messages on topic 'tp-iot' (will exit after 20s of inactivity)...")
for msg in consumer:
    print("recv:", msg.value)

print("consumer finished (timeout or no more messages).")
