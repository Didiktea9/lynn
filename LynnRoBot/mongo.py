import asyncio
import sys


from LynnRoBot import MONGO_DB_URI 
from pymongo import MongoClient

from LynnRoBot.conf import get_int_key, get_str_key


MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "DaisyX"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
db = client["LynnRoBot"]
