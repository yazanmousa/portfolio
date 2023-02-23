import pymongo
from pymongo import MongoClient
import pandas as pd
import ssl

uri='mongodb://localhost:27017'

client = MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)


client.list_database_names()

db=client.spotify

df=pd.read_csv("playlists.csv")

db.population.insert_many(df.to_dict())