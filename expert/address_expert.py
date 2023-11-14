from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')
filter={
    "address": "Thành phố Hồ Chí Minh"
}

result = client['essme']['experts_vn'].find(
  filter=filter
)

for document in result:
    try:
        document["address"] = "Hanoi"
        filter_1 = {"_id": document["_id"]}
        client['essme']['experts_vn'].replace_one(filter_1,document)
    except Exception:
        print(document["_id"], "error");
    