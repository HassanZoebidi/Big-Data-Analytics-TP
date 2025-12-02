# consumer_analysis.py
# Consumes messages from 'tp-iot', prints them and logs anomalies (temperature>80) to CSV.
# Usage:
#   pip install kafka-python
#   python consumer_analysis.py

import csv, time, json, os
from kafka import KafkaConsumer

BOOTSTRAP = ['localhost:19092','localhost:29092','localhost:39092']
topic = 'tp-iot'
csvfile = 'anomalies.csv'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=BOOTSTRAP,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    consumer_timeout_ms=10000
)

print("Listening for messages on topic 'tp-iot' (timeout after 10s of inactivity)...")
if not os.path.exists(csvfile):
    with open(csvfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ts','device_id','temperature','humidity','seq'])

for msg in consumer:
    data = msg.value
    print("recv:", data)
    try:
        temp = float(data.get('temperature', 0))
    except Exception:
        temp = 0.0
    if temp > 80.0:
        print("ANOMALY detected:", data)
        with open(csvfile, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([data.get('ts'), data.get('device_id'), data.get('temperature'), data.get('humidity'), data.get('seq')])

print("consumer finished (timeout or no more messages).")