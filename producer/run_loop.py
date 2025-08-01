import random, time
from datetime import datetime
from kafka_producer import produce_event, stats, producer
from event_generators import generate_click_event, generate_checkout_event
from stats import print_stats

def run(valid_customers, valid_products, duration_minutes=10, unknown_rate=0.05):
    start_time = datetime.now()
    duration_seconds = duration_minutes * 60
    
    while (datetime.now() - start_time).seconds < duration_seconds:
        try:
            customer_id = random.choice(valid_customers)
            product_id = random.choice(valid_products)

            # Click event
            click_event = generate_click_event(customer_id, product_id)
            if produce_event("clicks", click_event):
                print(f"[CLICK] {customer_id} - {product_id}")

            # Checkout 70% of the time
            if random.random() > 0.3:
                checkout_event = generate_checkout_event(customer_id, product_id)
                if produce_event("checkouts", checkout_event):
                    print(f"[CHECKOUT] {customer_id} - {product_id}")

            if (stats['successful_events'] + stats['failed_events']) % 50 == 0:
                print_stats()

            time.sleep(1.5)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(1)
    
    print("\nFlushing messages…")
    producer.flush()
    print_stats()
