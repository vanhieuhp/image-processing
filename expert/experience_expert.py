from pymongo import MongoClient
import re
import random

client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')
filter={
    'experience': None
}

expericen_array = [
    "3 - 5 years",
    "5 - 10 years",
    "> 10 years",
]

result = client['essme']['experts_vn'].find(
  filter=filter
)

for document in result:
    try:
        random_integer = random.randint(0, 2)
        document["experience"] = expericen_array[random_integer]
        filter_1 = {"_id": document["_id"]}
        client['essme']['experts_vn'].replace_one(filter_1,document)
    except Exception:
        print(document["_id"], "error");
    