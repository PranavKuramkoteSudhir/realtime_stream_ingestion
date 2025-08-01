producer_config = {
    'bootstrap.servers': 'localhost:9092',
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
    'host': 'localhost',
    'port': 5432,
    'user': 'user',
    'password': 'password',
    'dbname': 'mydb'
}
