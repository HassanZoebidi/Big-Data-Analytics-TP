
#  Big Data TP2 – E-Commerce Behavior Analysis  
**Author:** Hassan Zoebidi  
**University:** Hamma Lakhdar University – Master 2 AI & Data Science  
**Academic Year:** 2025  

---

##  Project Overview
This project demonstrates how to efficiently **process and analyze a large-scale dataset (≈5.3 GB)** from a real-world **multi-category e-commerce store**.  
The dataset, titled **“E-Commerce Behavior Data from Multi-Category Store (October 2019)”**, contains **over 42 million events** (pageviews, purchases, cart additions, etc.) collected from an online shop.

The main goal is to **evaluate the performance of different Big Data handling techniques in Python**, focusing on:
- Execution time  
- Memory consumption  
- Storage efficiency  

---

##  Dataset Description
**Source:** [Kaggle – E-Commerce Behavior Data (2019-Oct.csv)](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

**Size:** ~5.28 GB  
**Rows:** 42,448,764  
**Columns include:**
- `event_time`: Timestamp of the user action  
- `event_type`: Type of action (`view`, `cart`, `purchase`)  
- `product_id`, `category_id`, `category_code`  
- `brand`, `price`, `user_id`, `user_session`  

This dataset simulates a **real-world e-commerce environment**, making it ideal for testing **Big Data processing performance**.

---

##  Tools & Technologies
| Tool | Purpose |
|------|----------|
| **Python 3.13** | Main programming environment |
| **Pandas** | Chunked CSV reading and data aggregation |
| **Dask** | Parallel processing for distributed computation |
| **PyArrow / Parquet** | Columnar storage and efficient compression |
| **GZIP** | File compression (reduces size with minimal CPU overhead) |
| **Psutil** | Monitoring memory and CPU usage |

---

##  Script: `benchmark_bigdata.py`
This Python script benchmarks several methods for processing the massive CSV file.

### **Main Methods Tested**
1. **Pandas (Chunked Reading)**  
   - Reads CSV in chunks (e.g., 1,000,000 rows)  
   - Balances speed and memory usage  

2. **Pandas + GZIP (Compressed CSV)**  
   - Reads compressed `.csv.gz` file  
   - Smaller storage size, slightly slower  

3. **Dask DataFrame**  
   - Parallel reading of the dataset  
   - Ideal for distributed systems but heavy on RAM  

4. **Parquet Conversion**  
   - Converts CSV → Parquet (Snappy compression)  
   - Best for storage and future analytical speed  

---

##  Usage

### **1. Configuration**
Edit the following lines in `benchmark_bigdata.py`:
```python
RAW_CSV = Path(r"C:\path\to\2019-Oct.csv")
NUM_COLS = ["price"]
CHUNKSIZE = 1_000_000
```

### **2. Run the script**
```bash
python benchmark_bigdata.py
```

### **3. Output Example**
```
=== STORAGE (before) ===
Raw CSV: 5.28 GB

[Method A] Pandas chunks
Elapsed: 88.79s   Peak mem: 387 MB

[Method C] Pandas gzip + chunks
Elapsed: 112.05s  Peak mem: 353 MB

[Method B] Dask DataFrame
Elapsed: 416.06s  Peak mem: 18.28 GB

Writing Parquet (snappy)...
Parquet dir: 1.35 GB
```

---

##  Results Summary
| Method | Execution Time | Peak Memory | File Size | Notes |
|---------|----------------|--------------|------------|--------|
| Pandas (chunks) | 88.79 s | 387 MB | — | Fastest, efficient |
| Pandas + GZIP | 112.05 s | 353 MB | 1.62 GB | Good compression |
| Dask | 416.06 s | 18.28 GB | — | High memory use |
| Parquet (Snappy) | — | — | 1.35 GB | Best compression |

---

##  Analysis
- **Pandas with chunksize** gives the best balance for single-machine environments.  
- **Dask** is powerful for distributed systems but heavy on RAM.  
- **GZIP** reduces file size by ~69% with only a small performance penalty.  
- **Parquet** is the most space-efficient and fastest for analytics.

---

##  Recommendations
- For **single-machine projects**: use **Pandas with chunksize**.  
- For **distributed environments**: use **Dask** or **Apache Spark**.  
- For **long-term storage**: convert to **Parquet (Snappy)**.  
- Use **ZSTD or Brotli** for potential future compression improvements.

---

##  Future Work
1. Test on a multi-node cluster (e.g., Apache Spark).  
2. Add exploratory statistics (mean, median, missing values).  
3. Compare read/write speeds for different compression formats.  
4. Integrate visualization dashboards (Power BI or Plotly).

---

##  License
Dataset provided by **Mikhail Kechinov** under **CC BY-NC-SA 4.0 License** on Kaggle.
