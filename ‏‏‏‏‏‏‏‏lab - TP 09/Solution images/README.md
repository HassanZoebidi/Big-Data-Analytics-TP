#  مشروع WordCount باستخدام Apache Spark (Batch & Streaming)

## 🧩 وصف المشروع
يهدف هذا المشروع إلى التعرف على أساسيات **Apache Spark** من خلال:
- معالجة البيانات على دفعات (**Batch Processing**)
- معالجة البيانات المتدفقة (**Structured Streaming**)
- العمل داخل حاوية **Docker**

---

## 🛠️ المتطلبات
- Docker
- PowerShell (صلاحيات Administrator)
- اتصال بالإنترنت

---

## 🚀 إعداد البيئة

### تشغيل PowerShell كمسؤول
```bash
docker run -u 0 -it --name mon-spark -h spark-master apache/spark:3.5.0 /bin/bash
```

### تثبيت الأدوات داخل الحاوية
```bash
apt-get update && apt-get install -y nano maven netcat-openbsd openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

---

## 📁 هيكلة المشروع
```bash
mkdir -p wordcount-spark/src/main/java/spark/batch/tp21
mkdir -p wordcount-spark/src/main/java/spark/streaming/tp22
cd wordcount-spark
```

---

## 📦 pom.xml
```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>spark.batch</groupId>
  <artifactId>wordcount-spark</artifactId>
  <version>1.0-SNAPSHOT</version>
  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.apache.spark</groupId>
      <artifactId>spark-core_2.12</artifactId>
      <version>3.5.0</version>
    </dependency>
    <dependency>
      <groupId>org.apache.spark</groupId>
      <artifactId>spark-streaming_2.12</artifactId>
      <version>3.5.0</version>
    </dependency>
    <dependency>
      <groupId>org.apache.spark</groupId>
      <artifactId>spark-sql_2.12</artifactId>
      <version>3.5.0</version>
    </dependency>
  </dependencies>
</project>
```

---

## 🧮 WordCount Batch
```java
package spark.batch.tp21;
...
```

---

## 🌐 WordCount Streaming
```java
package spark.streaming.tp22;
...
```

---

## 📦 بناء المشروع
```bash
mvn package
```

---

## 🧪 تشغيل Batch
```bash
echo "Hello Spark Hello Big Data Hello Hassan" > input.txt
/opt/spark/bin/spark-submit --class spark.batch.tp21.WordCountTask --master local[*] wordcount-spark/target/wordcount-spark-1.0-SNAPSHOT.jar input.txt output_result
```

---

## 🔄 تشغيل Streaming
### النافذة الأولى
```bash
docker exec -it mon-spark nc -lk 9999
```

### النافذة الثانية
```bash
docker exec -it mon-spark /opt/spark/bin/spark-submit --class spark.streaming.tp22.Stream --master local[*] wordcount-spark/target/wordcount-spark-1.0-SNAPSHOT.jar
```

---
