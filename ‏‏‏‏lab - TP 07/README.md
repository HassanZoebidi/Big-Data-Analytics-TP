# مشروع إنترنت الأشياء + كافكا — README

## 1. المقدمة
هذا المشروع يهدف إلى بناء نظام بسيط لمعالجة بيانات أجهزة إنترنت الأشياء (IoT) باستخدام **Apache Kafka** على نظام Windows عبر **Docker**.  
الهدف هو محاكاة أجهزة تقوم بإرسال بيانات (درجة الحرارة، الرطوبة...) إلى Kafka ثم تحليلها واكتشاف الحالات الشاذة (Anomalies).

---

## 2. المتطلبات
- Windows 10 أو أعلى  
- Docker Desktop  
- Python 3.9+  
- مكتبة kafka-python  
```
pip install kafka-python
```

---

## 3. بنية المشروع
```
kafka-cluster/
│  docker-compose.yml
│  anomalies.csv   (يُنشئه المستهلك التحليلي تلقائياً)
│
├── iot_producer_cluster.py
├── iot_multi_producer.py
└── consumer_analysis.py
```

---

## 4. تثبيت وتشغيل Apache Kafka على Windows (باستخدام Docker)

تشغيل الكلاستر:
```
docker-compose up -d
docker ps
```

---

## 5. إنشاء Topic داخل Kafka
```
kafka-topics.sh --create --topic tp-iot --bootstrap-server localhost:19092 --partitions 3 --replication-factor 3
```

التحقق من الـ Topic:
```
kafka-topics.sh --describe --topic tp-iot --bootstrap-server localhost:19092
```

---

## 6. المنتج والمستهلك (Python)

### المنتج البسيط:
```
python iot_producer_cluster.py
```

### المستهلك التحليلي:
```
python consumer_analysis.py
```

---

## 7. محاكاة جهاز IoT متعدد (5 أجهزة)
```
python iot_multi_producer.py
```

كل جهاز يرسل 50 رسالة تحتوي:
- Temperature  
- Humidity  
- Device ID  
- Timestamp  

---

## 8. كشف الشذوذ (Anomaly Detection)

المستهلك التحليلي يقوم بـ:
- قراءة كل رسالة قادمة من Kafka  
- إذا كانت الحرارة > 80 → يتم اعتباره **خلل/عطل**  
- يتم تسجيله في ملف:  
```
anomalies.csv
```

---

## 9. نتائج المشروع
- تشغيل كافكا بنجاح داخل Docker  
- تهيئة Cluster مكون من 3 Brokers + Controller  
- إنشاء Topic بقدرة تكرار Replication=3  
- إرسال رسائل IoT عبر المنتج  
- استقبال رسائل وتحليلها عبر المستهلك  
- اكتشاف الأعطال وتسجيلها في CSV  

---

## 10. أوامر مفيدة
```
docker-compose down
docker logs kafka-broker-1
docker exec -it kafka-broker-1 bash
```

---

## 11. تحسينات مستقبلية
- إضافة لوحة مراقبة باستخدام Grafana  
- تخزين البيانات في قاعدة NoSQL  
- استخدام Machine Learning للكشف التنبؤي عن الأعطال  

---

مشروع مبني باستخدام: **Apache Kafka 4.1.1**, **Docker**, **Python**.
