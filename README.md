# realtime_stream_ingeswtion
Flink and kafka based data ingestion pipeline


## Introduction
This project provides a **streaming ingestion platform** designed to collect, process, and analyze data in real time.  
The stack is fully containerized using **Docker Compose**, making it easy to run locally for development, testing, or demonstration purposes.

The key goals of this project:
- Set up a robust **event streaming pipeline** using Kafka.
- Store structured data in **PostgreSQL**.
- Enable powerful search and analytics through **Elasticsearch**.
- Provide visualizations and dashboards using **Kibana**.
- Serve as a foundation for adding future data processing frameworks like Flink, Spark, or Airflow.

---

## Architecture Overview

+---------------+-------------+ Producers | -----> | Kafka | ----+--------------+--------------+
| | | | | | |
| | | v | | |
| | | +----------------+ | | |
| PostgreSQL | <-----------+ | Kibana | <-----+ Elasticsearch| <---- Queries|
+---------------+-------------+ +--------------+--------------+

---

## Tech Stack

- **Kafka** – The event streaming backbone for real-time messages.
- **Zookeeper** – Coordinates the Kafka broker (Zookeeper mode).
- **PostgreSQL** – A relational database for structured data.
- **Elasticsearch** – For indexing and searching large volumes of events.
- **Kibana** – A UI layer for dashboards, search, and visualizations.
- **Docker Compose** – Orchestrates all the services for easy local setup.

---
