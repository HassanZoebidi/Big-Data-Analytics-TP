# iot_multi_producer.py
# Simulates 5 IoT devices sending messages in parallel to topic 'tp-iot'.
# Each device sends a message every 0.5s. Stops after 'messages_per_device' each.
# Usage:
#   pip install kafka-python
#   python iot_multi_producer.py

import time, json, random, threading
from kafka import KafkaProducer

BOOTSTRAP = ['localhost:19092','localhost:29092','localhost:39092']
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

topic = 'tp-iot'
devices = 5
messages_per_device = 50
interval_sec = 0.5

def device_thread(device_id):
    for i in range(messages_per_device):
        msg = {
            "device_id": f"device-{device_id}",
            "temperature": round(20 + random.random()*100, 2),  # allows occasional high temps
            "humidity": round(30 + random.random()*50, 2),
            "seq": i+1,
            "ts": int(time.time())
        }
        producer.send(topic, value=msg)
        if i % 10 == 0:
            print(f"device-{device_id} sent seq {i+1}")
        time.sleep(interval_sec)

threads = []
for d in range(1, devices+1):
    t = threading.Thread(target=device_thread, args=(d,), daemon=True)
    threads.append(t)
    t.start()

# wait for threads to finish
for t in threads:
    t.join()

producer.flush()
print("all devices finished sending")