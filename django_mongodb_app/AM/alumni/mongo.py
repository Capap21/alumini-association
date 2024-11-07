# alumni/mongo.py
from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_URI)
db = client['alumni_database']
alumni_collection = db['alumni']
