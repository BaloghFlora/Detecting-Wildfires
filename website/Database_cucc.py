from flask import Flask
from pymongo.mongo_client import MongoClient
import requests
import json
from bson import ObjectId



Database = Flask(__name__)


uri = "mongodb+srv://NEjjjO:fuckyou69@shoby0.bcrmqu3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)


data = client.Mindenis




fire = data.Minden

fire_kicsi = data.Minden #rovid

fire = data.EarthData24H



def GetDataFromDb():
    list = []
    for fires in fire_kicsi.find():
        list.append(fires)
    return list
