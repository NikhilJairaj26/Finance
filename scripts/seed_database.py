import json
import csv
from pymongo import MongoClient
import os

# Add the parent directory to the path to allow imports from the backend app
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.config import settings
from backend.app.utils.auth import get_password_hash

client = MongoClient(settings.DATABASE_URL)
db = client.get_database()

script_dir = os.path.dirname(os.path.abspath(__file__))

def seed_users():
    """Seeds the users collection with sample data."""
    print("Seeding users...")
    db.users.drop()
    users_path = os.path.join(script_dir, '../data/sample_users.json')
    with open(users_path, 'r') as f:
        users = json.load(f)
        for user in users:
            user['hashed_password'] = get_password_hash('password123') # Set a default password
            db.users.insert_one(user)
    print("Users seeded.")

def seed_transactions():
    """Seeds the transactions collection with sample data."""
    print("Seeding transactions...")
    db.transactions.drop()
    transactions_path = os.path.join(script_dir, '../data/sample_transactions.csv')
    with open(transactions_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['amount'] = float(row['amount'])
            row['income'] = int(row['income'])
            row['age'] = int(row['age'])
            db.transactions.insert_one(row)
    print("Transactions seeded.")

if __name__ == "__main__":
    seed_users()
    seed_transactions()
    print("Database seeding complete!")
