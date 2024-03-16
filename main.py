import json
from pymongo import MongoClient

#connects to server
client = MongoClient('mongodb://localhost:27017/')

# create database
db = client['mydatabase']

# create collection inside database
collection = db['mycollection']

# opens json
with open('city_inspections.json', 'r') as f:
    for line in f:
        # load every line
        document = json.loads(line)

        # remove the '$oid' field from the '_id' field
        document['_id'] = document['_id']['$oid']

        # insert into collection
        collection.insert_one(document)

