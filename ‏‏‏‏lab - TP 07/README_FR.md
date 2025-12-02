# Projet IoT + Kafka — README

## 1. Introduction
Ce projet met en place un système IoT basé sur Apache Kafka utilisant Docker sous Windows.  
Objectif : Simuler des capteurs IoT envoyant des données vers Kafka, analyser les messages et détecter des anomalies.

## 2. Prérequis
- Windows 10+
- Docker Desktop
- Python 3.9+
- kafka-python :
```
pip install kafka-python
```

## 3. Architecture du Projet
```
kafka-cluster/
│ docker-compose.yml
│ anomalies.csv
│
├── iot_producer_cluster.py
├── iot_multi_producer.py
└── consumer_analysis.py
```

## 4. Installation Kafka sous Windows (Docker)
Lancement du cluster Kafka (Controller + Brokers) :
```
docker-compose up -d
docker ps
```

## 5. Création d’un Topic Kafka
```
kafka-topics.sh --create --topic tp-iot --bootstrap-server localhost:19092 --partitions 3 --replication-factor 3
```

Vérification :
```
kafka-topics.sh --describe --topic tp-iot --bootstrap-server localhost:19092
```

## 6. Producteur & Consommateur (Python)
### Producteur simple :
```
python iot_producer_cluster.py
```

### Consommateur simple :
```
python consumer_analysis.py
```

## 7. Simulation IoT Multi‑Devices
```
python iot_multi_producer.py
```

Envoie 5 × 50 messages avec valeurs variables (température, humidité…).

## 8. Détection d’Anomalies
Le consommateur analyse :
- Température > 80 → `ANOMALY`
- Enregistrement dans `anomalies.csv`

## 9. Résultats
- Cluster Kafka opérationnel
- Envoi & réception de messages IoT
- Détection d’anomalies
- Fichier CSV généré pour analyse

## 10. Commandes utiles
```
docker-compose down
docker logs kafka-broker-1
docker exec -it kafka-broker-1 bash
```

## 11. Améliorations futures
- Tableau de bord Grafana
- Sauvegarde dans base NoSQL
- Modèle ML pour détection intelligente

---

Projet réalisé avec : **Apache Kafka 4.1.1**, **Docker**, **Python**.
