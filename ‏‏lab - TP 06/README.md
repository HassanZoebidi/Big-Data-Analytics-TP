# README -- Running Docker + Cassandra & Solutions (EN + AR)

## 1. Running Cassandra with Docker

###  English

To start a Cassandra server using Docker, run:

``` bash
docker run -d --name cassandra -p 9042:9042 cassandra:latest
```

To check if the container is running:

``` bash
docker ps
```

To enter cqlsh:

``` bash
docker exec -it cassandra cqlsh
```

To copy CSV files into the container:

``` bash
docker cp path/to/restaurants.csv cassandra:/
docker cp path/to/restaurants_inspections.csv cassandra:/
```

------------------------------------------------------------------------

###  العربية

لتشغيل خادم كاساندرا باستخدام دوكر، نفّذ:

``` bash
docker run -d --name cassandra -p 9042:9042 cassandra:latest
```

للتحقق من أن الحاوية تعمل:

``` bash
docker ps
```

لدخول cqlsh:

``` bash
docker exec -it cassandra cqlsh
```

لنسخ ملفات CSV داخل الحاوية:

``` bash
docker cp path/to/restaurants.csv cassandra:/
docker cp path/to/restaurants_inspections.csv cassandra:/
```

------------------------------------------------------------------------

## 2. Importing Data in Cassandra

Inside **cqlsh**, select the keyspace:

``` sql
USE resto_NY;
```

Then import files:

``` sql
COPY Restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype)
FROM '/restaurants.csv' WITH DELIMITER=',' AND HEADER=TRUE;

COPY Inspection (idrestaurant, inspectiondate, violationcode, violationdescription, criticalflag, score, grade)
FROM '/restaurants_inspections.csv' WITH DELIMITER=',' AND HEADER=TRUE;
```

------------------------------------------------------------------------

# 3. Questions + Answers (English + Arabic + Solution)

------------------------------------------------------------------------

# 1. List of all restaurants

### بالعربية: قائمة بجميع المطاعم

``` sql
SELECT * FROM Restaurant;
```

------------------------------------------------------------------------

# 2. List of restaurant names

### بالعربية: قائمة أسماء المطاعم فقط

``` sql
SELECT name FROM Restaurant;
```

------------------------------------------------------------------------

# 3. Name and borough of the restaurant with id = 41569764

### بالعربية: اسم وحي المطعم الذي يحمل المعرف 41569764

``` sql
SELECT name, borough
FROM Restaurant
WHERE id = 41569764;
```

------------------------------------------------------------------------

# 4. Inspection dates and grades for this same restaurant

### بالعربية: تواريخ ودرجات التفتيش لهذا المطعم

``` sql
SELECT inspectiondate, grade
FROM Inspection
WHERE idrestaurant = 41569764;
```

------------------------------------------------------------------------

# 5. Names of restaurants serving French cuisine

### بالعربية: أسماء المطاعم ذات المطبخ الفرنسي

``` sql
SELECT name
FROM Restaurant
WHERE cuisinetype = 'French';
```

------------------------------------------------------------------------

# 6. Names of restaurants located in BROOKLYN

### بالعربية: أسماء المطاعم الموجودة في BROOKLYN

If an error appears, it is because **borough** is not indexed.

### Solution 1 (Recommended):

``` sql
CREATE INDEX idx_rest_borough ON Restaurant (borough);

SELECT name
FROM Restaurant
WHERE borough = 'BROOKLYN';
```

### Solution 2 (ALLOW FILTERING):

``` sql
SELECT name
FROM Restaurant
WHERE borough = 'BROOKLYN'
ALLOW FILTERING;
```

------------------------------------------------------------------------

# 7. Grades and scores for restaurant 41569764 with score ≥ 10

### بالعربية: الدرجات والسكورات للمطعم 41569764 بشرط أن يكون السكور ≥ 10

``` sql
SELECT grade, score
FROM Inspection
WHERE idrestaurant = 41569764 AND score >= 10
ALLOW FILTERING;
```

------------------------------------------------------------------------

# 8. Non-null grades where score \> 30

### بالعربية: الدرجات غير الفارغة للتفتيشات التي يكون السكور فيها \> 30

Cassandra does not support `grade IS NOT NULL` on a non-indexed column.

### Valid Query:

``` sql
SELECT grade
FROM Inspection
WHERE score > 30
ALLOW FILTERING;
```

After removing null values manually, the non-null grades are:

    A, B, C, P, Z

------------------------------------------------------------------------

# 9. Number of rows returned by the previous query

### بالعربية: عدد الصفوف المُرجعة من الاستعلام السابق

The query:

``` sql
SELECT grade
FROM Inspection
WHERE score > 30
ALLOW FILTERING;
```

Returned:

    (8729 rows)

So the number of rows is:

    8729

------------------------------------------------------------------------

