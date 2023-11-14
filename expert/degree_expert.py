from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')

# Access the desired collection
db = client['essme']
collection = db['experts_vn']

filter={'degree': 'Research student'}
update = {'$set': {'degree': "Master"}}

result = collection.update_many(filter, update)

print('Documents updated: ', result.modified_count)