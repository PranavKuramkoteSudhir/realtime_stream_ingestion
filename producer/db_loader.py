import psycopg2
from config import postgres_config

def load_valid_ids():
    try:
        conn = psycopg2.connect(**postgres_config)
        cursor = conn.cursor()

        cursor.execute("SELECT customer_id FROM commerce.customers")
        customers = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT product_id FROM commerce.products")
        products = [row[0] for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        print(f"Loaded {len(customers)} customers and {len(products)} products")
        return customers, products
    except Exception as e:
        print(f"DB load failed: {e}")
        print("Falling back to dummy ranges...")
        customers = [f"u{i:07d}" for i in range(2025001, 2025101)]
        products = [f"p0{i}" for i in range(1341, 1361)]
        return customers, products
