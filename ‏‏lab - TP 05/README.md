# TP رقم 5 — MongoDB (شرح + أوامر + نتائج)

الطالب: **HASSAN ZOEBIDI**  
التخصص: **IA**

---

## 1) المطلوب من الـ TP

الـ TP يطلب:

1. تثبيت MongoDB
2. تشغيل mongod
3. تشغيل mongo
4. إنشاء قاعدة بيانات info
5. إنشاء collection produits
6. إضافة 3 منتجات
7. تنفيذ استعلامات READ
8. تنفيذ DELETE
9. عرض النتائج

---

## 2) تثبيت MongoDB

قمت بتحميل النسخة:

```
mongodb-win32-x86_64-2008plus-2.6.4
```

وأنشأت المجلدات:

```
C:\data
C:\data\db
```

---

## 3) تشغيل خادم MongoDB

```
C:\mongodb-win32-x86_64-2008plus-2.6.4\bin\mongod.exe
```

النتيجة:

```
waiting for connections on port 27017
```

---

## 4) تشغيل mongo shell

```
C:\mongodb-win32-x86_64-2008plus-2.6.4\bin\mongo.exe
```

النتيجة:

```
MongoDB shell version: 2.6.4
connecting to: test
>
```

---

## 5) إنشاء قاعدة البيانات

```
use info
```

---

## 6) إضافة المنتجات INSERT

### Macbook Pro

```js
db.produits.insert({
  nom: "Macbook Pro",
  fabriquant: "Apple",
  prix: 11435.99,
  options: ["Intel Core i5", "Retina Display", "Long life battery"]
})
```

### Macbook Air

```js
db.produits.insert({
  nom: "Macbook Air",
  fabriquant: "Apple",
  prix: 125794.73,
  ultrabook: true,
  options: ["Intel Core i7", "SSD", "Long life battery"]
})
```

### Thinkpad X230

```js
db.produits.insert({
  nom: "Thinkpad X230",
  fabriquant: "Lenovo",
  prix: 114358.74,
  ultrabook: true,
  options: ["Intel Core i5", "SSD", "Long life battery"]
})
```

---

## 7) استعلامات READ

### عرض كل المنتجات

```
db.produits.find()
```

### أول منتج

```
db.produits.findOne()
```

### إيجاد Thinkpad X230

```
db.produits.find({ nom: "Thinkpad X230" })
```

### منتجات سعرها أكبر من 13723

```
db.produits.find({ prix: { $gt: 13723 } })
```

### أول ultrabook

```
db.produits.findOne({ ultrabook: true })
```

### منتج يحتوي "Macbook"

```
db.produits.findOne({ nom: /Macbook/ })
```

### منتجات تبدأ بـ Macbook

```
db.produits.find({ nom: /^Macbook/ })
```

---

## 8) عمليات DELETE

### حذف منتجات Apple

```
db.produits.remove({ fabriquant: "Apple" })
```

### حذف Thinkpad X230 بالـ ID

```
db.produits.remove({ _id: ObjectId("691c3486b13570e3ecc211a8") })
```

---

## الخلاصة

✓ إنشاء DB  
✓ إنشاء Collection  
✓ إضافة 3 مستندات  
✓ تنفيذ استعلامات  
✓ تنفيذ حذف  
✓ إكمال TP بنجاح 100%

---

