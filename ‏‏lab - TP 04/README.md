
# 🐳 TP04 – Dockerized Power BI Project

**Author:** Hassan Zoebidi  
**Subject:** Big Data – TP04 (Docker)  
**Date:** November 2025  

---

## 📘 Project Overview

This project demonstrates how to containerize a Power BI report using Docker and Python Flask.  
The Power BI report (`TP_03.pbix`) is served inside a Docker container.  
Users can access the report through a simple web interface and download it.

---

## ⚙️ Technologies Used

- Docker Desktop  
- Python 3.10 (Slim Image)  
- Flask Web Framework  
- Power BI Report (`TP_03.pbix`)

---

## 🧱 Project Structure

\`\`\`
TP4/
 ├── Dockerfile
 ├── TP_03.pbix
 └── README.md
\`\`\`

---

## 🧩 Dockerfile Explanation

\`\`\`dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY TP_03.pbix .

RUN pip install flask

RUN echo "from flask import Flask, send_file\n\
app = Flask(__name__)\n\
@app.route('/')\n\
def home():\n\
    return '<h2>TP3 Power BI Report</h2><a href=\"/download\">Download TP3.pbix</a>'\n\
@app.route('/download')\n\
def download():\n\
    return send_file('TP_03.pbix', as_attachment=True)\n\
if __name__ == '__main__':\n\
    app.run(host='0.0.0.0', port=5000)" > app.py

EXPOSE 5000

CMD ["python", "app.py"]
\`\`\`

---

## 🛠️ Build the Docker Image

\`\`\`bash
docker build -t hassanzoebidi/powerbi-tp3:v1 .
\`\`\`

---

## ▶️ Run the Container

\`\`\`bash
docker run -d -p 8080:5000 --name tp3container hassanzoebidi/powerbi-tp3:v1
\`\`\`

Then open:

👉 http://localhost:8080

You will see:

> TP3 Power BI Report  
> Download TP3.pbix

---

## ☁️ Publish to Docker Hub

\`\`\`bash
docker login
docker push hassanzoebidi/powerbi-tp3:v1
\`\`\`

Docker Hub Repository:  
👉 https://hub.docker.com/r/hassanzoebidi/powerbi-tp3

---

## 🌐 Create a Network and 3 Containers

### 1️⃣ Create network:
\`\`\`bash
docker network create tp3-network
\`\`\`

### 2️⃣ Run 3 containers attached to the same network:
\`\`\`bash
docker run -d -p 8081:5000 --name cont1 --network tp3-network hassanzoebidi/powerbi-tp3:v1
docker run -d -p 8082:5000 --name cont2 --network tp3-network hassanzoebidi/powerbi-tp3:v1
docker run -d -p 8083:5000 --name cont3 --network tp3-network hassanzoebidi/powerbi-tp3:v1
\`\`\`

### 3️⃣ Verify network:
\`\`\`bash
docker network inspect tp3-network
\`\`\`

---

## 📊 Verification

### List images:
\`\`\`bash
docker images
\`\`\`

### List containers:
\`\`\`bash
docker ps -a
\`\`\`

### Access containers:
- http://localhost:8081  
- http://localhost:8082  
- http://localhost:8083  

---

## ✅ Summary

- Successfully containerized Power BI report into a Docker image.  
- Created a lightweight Flask server to deliver the \`.pbix\` file.  
- Deployed 3 containers and connected them using a custom Docker bridge network.  
- Image is published publicly on Docker Hub.

---

**Author:** *Hassan Zoebidi*  
**Docker Hub:** https://hub.docker.com/r/hassanzoebidi/powerbi-tp3

