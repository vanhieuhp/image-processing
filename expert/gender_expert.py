from pymongo import MongoClient
import re
import random

client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')
filter={
    'display_name': {
        '$regex': re.compile(r"thi (?i)")
    }
}

result = client['essme']['experts_vn'].find(
  filter=filter
)

for document in result:
    try:
        document["gender"] = "Female"
        filter_1 = {"_id": document["_id"]}
        client['essme']['experts_vn'].replace_one(filter_1,document)
    except Exception:
        print(document["_id"], "error");
    