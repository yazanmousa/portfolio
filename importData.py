import pymongo
import pandas as pd
from pymongo import MongoClient
client = MongoClient()
db = client.spotify
collection = db.playlists
data = pd.DataFrame(list(collection.find()))
print(data)