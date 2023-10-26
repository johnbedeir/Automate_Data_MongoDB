import json
from pymongo import MongoClient

# Load the MongoDB connection configuration
with open('config.json', 'r') as file:
    config = json.load(file)

# Load the data to be inserted
with open('data.json', 'r') as file:
    document = json.load(file)

# Connect to the MongoDB instance
client = MongoClient(config['MONGODB_URI'])

# Select (or create) the database 'mydatabase'
db = client.surveyDB

# Select (or create) the collection 'mycollection'
collection = db.answers

# Insert the document
collection.insert_one(document)

print("Document inserted successfully!")

# Close the connection
client.close()
