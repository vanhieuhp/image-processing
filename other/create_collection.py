from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB server
client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')

# Access the desired collection
db = client['essme']
collection = db['qualification']
def read_file(filename):
    value = set()
    with open(filename, 'r') as file:
        for line in file:
           value.add(line.strip())
    return value


qualifications = read_file("data.txt")
for degree in qualifications:
    sample_document = {
        "degree": degree.capitalize(),
        "last_modified_date": datetime.now(),
        "created_date": datetime.now(),
        "category_id": "61de9e5c15a9c15d057dbb47",
        "deleted": False,
        "_class": "org.vietsearch.essme.db.model.Qualification"
    }
    collection.insert_one(sample_document)
            
# test_document = {
#     "last_modified_date": datetime.now(),
#     "created_date": datetime.now()
# }
# collection.insert_one(test_document)