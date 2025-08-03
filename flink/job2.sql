-- Insert into enriched_events from checkouts_raw (your new job)
INSERT INTO enriched_events
SELECT
    ch.eventType,
    ch.checkoutId AS eventId, -- Use checkoutId as the eventId for checkouts
    ch.customerId AS customer_id,
    COALESCE(cust.name, 'Unknown Customer') AS customer_name,
    ch.productId AS product_id,
    COALESCE(prod.name, 'Unknown Product') AS product_name,
    COALESCE(prod.brand, 'Unknown Brand') AS product_brand,
    COALESCE(prod.category, 'Unknown Category') AS product_category,
    ch.paymentMethod,          
    ch.quantity,               
    ch.totalAmount,            
    ch.userAgent,
    ch.ip_address,
    CAST(NULL AS STRING) AS url, 
    ch.datetime_occured AS event_time
FROM checkouts_raw ch
LEFT JOIN customer_dim cust
    ON ch.customerId = cust.customer_id
LEFT JOIN product_dim prod
    ON ch.productId = prod.product_id
WHERE ch.checkoutId IS NOT NULL;