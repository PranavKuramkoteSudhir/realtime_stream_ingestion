# Real-Time E-commerce Data Streaming Pipeline

A complete real-time data streaming pipeline that simulates e-commerce events (clicks and checkouts), enriches them with customer and product data, and indexes them for analytics.


![Screen Recording 2025-07-31 at 9 28 09 AM(1)](https://github.com/user-attachments/assets/a468dd67-8303-46f1-908c-f9ac0fdc5936)

## Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Producer  │───▶│    Kafka    │───▶│    Flink    │───▶│Elasticsearch│
│  (Python)   │    │  (Events)   │    │ (Enrichment)│    │  (Storage)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │ PostgreSQL  │
                                      │(Dimensions) │
                                      └─────────────┘
```

**Components:**
- **PostgreSQL**: Stores customer and product dimension data
- **Kafka**: Message broker for streaming click and checkout events  
- **Apache Flink**: Stream processing engine for real-time data enrichment
- **Elasticsearch**: Search and analytics engine for enriched events
- **Kibana**: Data visualization and dashboards
- **Python Producer**: Generates realistic e-commerce event data

## Features

- **Real-time Event Processing**: Handles click and checkout events with sub-second latency
- **Data Enrichment**: Joins streaming events with dimensional data (customer/product info)
- **Scalable Architecture**: Multiple Flink TaskManagers for parallel processing
- **Analytics Ready**: Events indexed in Elasticsearch for real-time dashboards
- **Realistic Data**: Uses Faker library to generate authentic e-commerce data

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- At least 4GB available RAM

## Quick Start

### 1. Clone and Setup

```bash
git clone <repository-url>
cd stream_commit
python -m venv venv
source venv/bin/activate
```

### 2. Environment Configuration

```bash
# Copy environment template
cp .env.template .env

# Edit .env with your preferred passwords and paths
# Update PROJECT_ROOT to match your actual project path
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Setup Script

```bash
chmod +x process.sh
./process.sh
```

This script will:
- Start all Docker services
- Download required Flink connector JARs
- Initialize PostgreSQL with schema and seed data
- Create Kafka topics
- Set up the processing pipeline

### 5. Configure Flink SQL (Manual Step Required)

Due to Flink SQL session requirements, you must manually set up the streaming jobs:

```bash
# Open Flink SQL client
docker exec -it flink-jobmanager ./bin/sql-client.sh

# In the SQL client, copy and paste ALL content from these files in order:
# 1. flink/schema_creation.sql (creates tables and catalog)
# 2. flink/job1.sql (click enrichment job)  
# 3. flink/job2.sql (checkout enrichment job)
```

### 6. Start Data Generation

```bash
python producer/trigger.py
```

## Project Structure

```
stream_commit/
├── db_conf/
│   ├── DB_init.sql          # PostgreSQL schema
│   └── seed.py              # Test data generation
├── producer/
│   ├── config.py            # Database and Kafka configs
│   ├── db_loader.py         # Loads valid customer/product IDs
│   ├── event_generators.py  # Creates realistic events
│   ├── kafka_producer.py    # Kafka message production
│   ├── run_loop.py          # Main event generation loop
│   ├── stats.py             # Performance statistics
│   └── trigger.py           # Entry point
├── flink/
│   ├── schema_creation.sql  # Flink table definitions
│   ├── job1.sql            # Click enrichment job
│   └── job2.sql            # Checkout enrichment job
├── docker-compose.yml       # Infrastructure definition
├── plugins.sh              # Downloads Flink connectors
├── process.sh              # Complete setup script
└── requirements.txt        # Python dependencies
```

## Data Flow

1. **Event Generation**: Python producer creates realistic click and checkout events
2. **Message Queuing**: Events are published to separate Kafka topics
3. **Stream Processing**: Flink consumes events and enriches them with PostgreSQL data
4. **Data Storage**: Enriched events are indexed in Elasticsearch
5. **Visualization**: Kibana provides real-time analytics dashboards

## Access Points

After setup completion:

- **Flink Dashboard**: http://localhost:8081
- **Kibana**: http://localhost:5601  
- **Elasticsearch API**: http://localhost:9200
- **PostgreSQL**: localhost:5432 (user/password from .env)

## Sample Data

- **Customers**: 100 users (IDs: u2025001-u2025100)
- **Products**: 20 items (IDs: p01341-p01360) 
- **Events**: Continuous click and checkout streams

## Monitoring

View real-time metrics:

```bash
# Kafka topics
docker exec -it broker kafka-topics --list --bootstrap-server broker:29092

# Flink jobs status
# Visit http://localhost:8081

# Elasticsearch indices
curl "localhost:9200/_cat/indices?v"

# Producer statistics
# Displayed in producer/trigger.py output
```

## Known Limitations

- **Flink Catalog Persistence**: Catalog configuration is not persistent and must be recreated after Flink restarts
- **Manual SQL Setup**: Flink SQL commands must be executed in a single session due to catalog limitations
- **Development Focus**: This setup is optimized for development and testing, not production use

## Future Improvements

- [ ] Persistent Flink catalog configuration
- [ ] Automated Flink job deployment
- [ ] Production-ready security configurations
- [ ] Schema registry integration
- [ ] Advanced monitoring and alerting
- [ ] Multi-environment configuration

## Troubleshooting

### PostgreSQL Issues
```bash
# If schema creation fails
docker exec -i postgres psql -U user -d mydb < ./db_conf/DB_init.sql

# Check database contents
docker exec -it postgres psql -U user -d mydb -c "SELECT COUNT(*) FROM commerce.customers;"
```

### Kafka Issues
```bash
# Recreate topics
docker exec -it broker kafka-topics --delete --topic clicks --bootstrap-server broker:29092
docker exec -it broker kafka-topics --create --topic clicks --partitions 3 --replication-factor 1 --bootstrap-server broker:29092
```

### Flink Issues
```bash
# Restart Flink cluster
docker compose restart jobmanager taskmanager taskmanager2

# Check connector JARs
docker exec -it flink-jobmanager ls /opt/flink/lib
```

## Contributing

This project demonstrates real-time data streaming concepts and is open for educational improvements and extensions.

## Security Notes

- Default passwords are used for development
- Elasticsearch security is disabled for simplicity
- PostgreSQL uses trust authentication locally
- Update credentials in `.env` for any non-local deployments
