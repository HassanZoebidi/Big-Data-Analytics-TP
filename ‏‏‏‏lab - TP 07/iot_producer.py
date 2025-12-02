# iot_producer.py
# Simple Kafka producer that sends 5 JSON messages to topic 'tp-iot'
# Usage:
#   pip install kafka-python
#   python iot_producer.py

import time, json, random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'tp-iot'

for i in range(5):
    message = {
        "device_id": f"device-{i+1}",
        "temperature": round(20 + random.random()*10, 2),
        "humidity": round(30 + random.random()*20, 2),
        "seq": i+1,
        "ts": int(time.time())
    }
    producer.send(topic, value=message)
    print("sent:", message)
    time.sleep(0.5)

producer.flush()
print("done sending 5 messages")
