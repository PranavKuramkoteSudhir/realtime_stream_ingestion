import random
from uuid import uuid4
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

def generate_click_event(customer_id, product_id):
    return {
        "eventType": "click",
        "clickId": str(uuid4()),
        "customerId": customer_id,
        "productId": product_id,
        "userAgent": fake.user_agent(),
        "ip_address": fake.ipv4(),
        "url": f"https://shop.example.com/product/{product_id}",
        "datetime_occured": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }

def generate_checkout_event(customer_id, product_id):
    qty = random.randint(1, 5)
    price = round(random.uniform(10.99, 999.99), 2)
    total = round(qty * price, 2)
    return {
        "eventType": "checkout",
        "checkoutId": str(uuid4()),
        "customerId": customer_id,
        "productId": product_id,
        "paymentMethod": random.choice(["credit_card", "debit_card", "paypal", "apple_pay", "google_pay"]),
        "quantity": qty,
        "totalAmount": total,
        "shippingAddress": fake.address().replace('\n', ', '),
        "billingAddress": fake.address().replace('\n', ', '),
        "userAgent": fake.user_agent(),
        "ip_address": fake.ipv4(),
        "datetime_occured": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }
