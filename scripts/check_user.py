import os
import sys
from pymongo import MongoClient

# Add the parent directory to the path to allow imports from the backend app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.config import settings

client = MongoClient(settings.DATABASE_URL)
db = client.get_database()

def check_user(email):
    user = db.users.find_one({"email": email})
    if user:
        print(f"User found: {user['email']}")
        print(f"Hashed password: {user['hashed_password']}")
    else:
        print(f"User with email {email} not found.")

if __name__ == "__main__":
    check_user("user1@example.com")
