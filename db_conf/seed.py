import psycopg2
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Database connection (using docker-exposed Postgres)
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="user",
    password="password",
    dbname="mydb"
)
cursor = conn.cursor()

def seed_customers(n=100):
    """Insert fake customers with custom IDs u2025001 - u2025100"""
    for i in range(1, n + 1):
        customer_id = f"u2025{str(i).zfill(3)}"  # u2025001 → u2025100
        name = fake.name()
        username = fake.unique.user_name()  # Changed to use unique
        email = fake.unique.email()
        phone = fake.phone_number()[:20]
        address = fake.address()
        
        cursor.execute("""
            INSERT INTO commerce.customers (customer_id, name, username, email, phone, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (customer_id, name, username, email, phone, address))

def seed_products(n=20):
    """Insert fake products with custom IDs p01341 - p01360"""
    categories = ['Electronics', 'Fashion', 'Grocery', 'Home', 'Beauty', 'Sports']
    brands = ['Apple', 'Samsung', 'Sony', 'Nike', 'Adidas', 'LG', 'Bose']
    
    for i in range(1, n + 1):
        product_id = f"p013{str(40 + i)}"  # p01341 → p01360
        name = fake.word().capitalize()
        description = fake.sentence(nb_words=10)
        category = random.choice(categories)
        brand = random.choice(brands)
        price = round(random.uniform(10, 1000), 2)
        currency = 'USD'
        
        cursor.execute("""
            INSERT INTO commerce.products (product_id, name, description, category, brand, price, currency)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (product_id, name, description, category, brand, price, currency))

# Seed the database
seed_customers(100)
seed_products(20)

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Seeded 100 customers (u2025001–u2025100) and 20 products (p01341–p01360) into Postgres!")