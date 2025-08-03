-- Register JDBC catalog
CREATE CATALOG pg_catalog WITH (
  'type' = 'jdbc',
  'default-database' = 'mydb',
  'username' = 'user',
  'password' = 'password',
  'base-url' = 'jdbc:postgresql://postgres:5432'
);

-- Define PostgreSQL tables (customer_dim, product_dim) in Flink SQL


CREATE TABLE customer_dim (
    customer_id STRING,       
    name STRING,             
    username STRING,          
    email STRING,             
    phone STRING,            
    address STRING,           
    created_at TIMESTAMP(3), 
    PRIMARY KEY (customer_id) NOT ENFORCED 
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://postgres:5432/mydb',
    'table-name' = 'commerce.customers',
    'username' = 'user',
    'password' = 'password'
);

CREATE TABLE product_dim (
    product_id STRING,        
    name STRING,              
    description STRING,       
    category STRING,          
    brand STRING,             
    price DECIMAL(10, 2),     
    currency STRING,          
    created_at TIMESTAMP(3),  
    PRIMARY KEY (product_id) NOT ENFORCED 
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://postgres:5432/mydb',
    'table-name' = 'commerce.products',
    'username' = 'user',
    'password' = 'password'
);

-- Create Kafka source tables (clicks_raw, checkouts_raw)
CREATE TABLE clicks_raw (
    eventType STRING,
    clickId STRING,
    customerId STRING,
    productId STRING,
    userAgent STRING,
    ip_address STRING,
    url STRING,
    datetime_occured STRING 
) WITH (
    'connector' = 'kafka',
    'topic' = 'clicks',
    'properties.bootstrap.servers' = 'broker:29092',
    'properties.group.id' = 'flink-sql',
    'format' = 'json',
    'scan.startup.mode' = 'latest-offset',
    'json.timestamp-format.standard' = 'ISO-8601'
);

CREATE TABLE checkouts_raw (
    eventType STRING,
    checkoutId STRING,
    customerId STRING,
    productId STRING,
    paymentMethod STRING,
    quantity INT,
    totalAmount DOUBLE,
    shippingAddress STRING,
    billingAddress STRING,
    userAgent STRING,
    ip_address STRING,
    datetime_occured STRING 
) WITH (
    'connector' = 'kafka',
    'topic' = 'checkouts',
    'properties.bootstrap.servers' = 'broker:29092',
    'properties.group.id' = 'flink-sql',
    'format' = 'json',
    'scan.startup.mode' = 'latest-offset',
    'json.timestamp-format.standard' = 'ISO-8601'
);

-- Create Elasticsearch sink table (enriched_events)
CREATE TABLE enriched_events (
    eventType STRING,
    eventId STRING,
    customer_id STRING,
    customer_name STRING,
    product_id STRING,
    product_name STRING,
    product_brand STRING,
    product_category STRING,
    paymentMethod STRING,
    quantity INT,
    totalAmount DOUBLE,
    userAgent STRING,
    ip_address STRING,
    url STRING,
    event_time STRING, 
    PRIMARY KEY (eventId) NOT ENFORCED
) WITH (
    'connector' = 'elasticsearch-8', 
    'hosts' = 'http://elasticsearch:9200',
    'index' = 'enriched-events'
);

