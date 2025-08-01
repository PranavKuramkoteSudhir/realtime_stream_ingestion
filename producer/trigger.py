from db_loader import load_valid_ids
from run_loop import run

if __name__ == "__main__":
    customers, products = load_valid_ids()
    run(customers, products, duration_minutes=10, unknown_rate=0.1)
