
---

##  الهدف من العمل
يهدف هذا العمل التطبيقي إلى فهم مبدأ **MapReduce** المستخدم في أنظمة معالجة البيانات الضخمة، وذلك من خلال محاكاة مراحله الأساسية (Map – Shuffle – Reduce) باستعمال لغة **Python** على منصة **Google Colab** بدون الحاجة إلى تثبيت Hadoop أو Spark.

تم تطبيق هذا المفهوم على **تحليل سجلات HTTP (Web Logs)** لاستخراج إحصائيات مختلفة.

---

##  ملخص النتائج (Results Summary)

### 1️⃣ عدد الطلبات حسب كود الحالة (Status Code)
```
HTTP 200: 10 requests
HTTP 403: 2 requests
HTTP 404: 5 requests
HTTP 500: 3 requests
```

### 2️⃣ عدد الطلبات حسب الرابط (URL)
```
/about.html: 2 requests
/checkout: 3 requests
/contact.html: 3 requests
/images/logo.png: 2 requests
/index.html: 5 requests
/login: 2 requests
/products.html: 3 requests
```

### 3️⃣ الحجم الإجمالي للاستجابة حسب كود الحالة
```
HTTP 200: 8182 bytes
HTTP 403: 128 bytes
HTTP 404: 2560 bytes
HTTP 500: 384 bytes
```

### 4️⃣ تحليل الأخطاء فقط (استبعاد الطلبات الناجحة 200)
```
HTTP 403: 2 requests
HTTP 404: 5 requests
HTTP 500: 3 requests
```

---

##  الدوال المطبقة (Implemented Functions)

###  دالة Mapper
```python
def mapper(line):
    fields = line.strip().split(',')
    if len(fields) != 7 or fields[0].startswith('#'):
        return []
    status = fields[5]
    return [(status, 1)]
```

###  دالة Shuffle
```python
from collections import defaultdict

def shuffle(mapped_data):
    grouped = defaultdict(list)
    for key, value in mapped_data:
        grouped[key].append(value)
    return grouped
```

###  دالة Reducer
```python
from collections import defaultdict

def reducer(mapped_data):
    grouped = defaultdict(int)
    for key, value in mapped_data:
        grouped[key] += value
    return grouped
```

---

##  تنفيذ البرنامج
```python
mapped = []
with open("weblogs.txt", "r") as f:
    for line in f:
        mapped.extend(mapper(line))

reduced = reducer(mapped)

for code, count in sorted(reduced.items()):
    print(f"HTTP {code}: {count} requests")
```

---

##  الخلاصة
من خلال هذا العمل، تم:
- فهم آلية عمل MapReduce عمليًا
- محاكاة معالجة البيانات الكبيرة باستخدام Python
- استخراج إحصائيات مفيدة من سجلات HTTP
- تطبيق مراحل Map، Shuffle، و Reduce بشكل واضح
