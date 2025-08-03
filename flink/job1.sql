-- Insert into enriched_events from clicks_raw (your existing job)
INSERT INTO enriched_events
SELECT
    c.eventType,
    c.clickId AS eventId,
    c.customerId AS customer_id,
    COALESCE(cust.name, 'Unknown Customer') AS customer_name,
    c.productId AS product_id,
    COALESCE(prod.name, 'Unknown Product') AS product_name,
    COALESCE(prod.brand, 'Unknown Brand') AS product_brand,
    COALESCE(prod.category, 'Unknown Category') AS product_category,
    CAST(NULL AS STRING) AS paymentMethod, 
    CAST(NULL AS INT) AS quantity,         
    CAST(NULL AS DOUBLE) AS totalAmount,   
    c.userAgent,
    c.ip_address,
    c.url,
    c.datetime_occured AS event_time
FROM clicks_raw c
LEFT JOIN customer_dim cust
    ON c.customerId = cust.customer_id
LEFT JOIN product_dim prod
    ON c.productId = prod.product_id
WHERE c.clickId IS NOT NULL; 

