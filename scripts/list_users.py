import os
import sys
from pymongo import MongoClient

# Add the parent directory to the path to allow imports from the backend app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.config import settings

client = MongoClient(settings.DATABASE_URL)
db = client.get_database()

def list_all_users():
    print("Listing all registered users:")
    users = db.users.find({})
    for user in users:
        print(f"  Email: {user.get('email')}, Full Name: {user.get('full_name')}")
    if db.users.count_documents({}) == 0:
        print("  No users found in the database.")

if __name__ == "__main__":
    list_all_users()
