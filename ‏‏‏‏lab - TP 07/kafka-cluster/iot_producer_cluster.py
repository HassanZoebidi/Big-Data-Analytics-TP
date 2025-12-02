# iot_producer_cluster.py
# Sends 5 JSON messages to topic 'tp-iot' using the multi-broker bootstrap servers.
# Usage:
#   pip install kafka-python
#   python iot_producer_cluster.py

import time, json, random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:19092','localhost:29092','localhost:39092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'tp-iot'

for i in range(5):
    message = {
        "device_id": f"device-{i+1}",
        "temperature": round(20 + random.random()*80, 2),
        "humidity": round(30 + random.random()*50, 2),
        "seq": i+1,
        "ts": int(time.time())
    }
    producer.send(topic, value=message)
    print("sent:", message)
    time.sleep(0.5)

producer.flush()
print("done sending 5 messages")
