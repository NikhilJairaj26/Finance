from pymongo import MongoClient
from .config import settings

client = MongoClient(settings.DATABASE_URL)
db = client.get_database()
