import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

producer_config = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
    'acks': 'all',
    'retries': 5,
    'retry.backoff.ms': 100,
    'batch.size': 16384,
    'linger.ms': 5,
    'compression.type': 'snappy',
    'request.timeout.ms': 30000,
    'delivery.timeout.ms': 60000,
    'max.in.flight.requests.per.connection': 1
}

postgres_config = {
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': int(os.getenv('POSTGRES_PORT', 5432)),
    'user': os.getenv('POSTGRES_USER', 'user'),
    'password': os.getenv('POSTGRES_PASSWORD', 'password'),
    'dbname': os.getenv('POSTGRES_DB', 'mydb')
}