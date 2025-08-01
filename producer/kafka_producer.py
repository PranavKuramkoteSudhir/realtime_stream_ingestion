import json, time
from confluent_kafka import SerializingProducer
from config import producer_config

producer = SerializingProducer(producer_config)

stats = {
    'successful_events': 0,
    'failed_events': 0,
    'validation_failures': 0,
    'unknown_customer_events': 0,
    'unknown_product_events': 0
}

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed for {msg.topic()}: {err}")
        stats['failed_events'] += 1
    else:
        stats['successful_events'] += 1
        if stats['successful_events'] % 10 == 0:
            print(f"Delivered {stats['successful_events']} events successfully")

def produce_event(topic, event):
    try:
        event_id = event.get('clickId') or event.get('checkoutId')
        producer.produce(
            topic,
            key=event_id,
            value=json.dumps(event),
            on_delivery=delivery_report
        )
        producer.poll(0)
        return True
    except Exception as e:
        print(f"Error producing to {topic}: {e}")
        return False
