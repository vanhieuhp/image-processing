from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')
filter={}

result = client['essme']['experts_vn'].find(
  filter=filter
)

for document in result:
    try:
        for index in range(len(document["research_area"])):
            document["research_area"][index] = document["research_area"][index].capitalize()
        for index in range(len(document["research_area_en"])):
            document["research_area_en"][index] = document["research_area_en"][index].capitalize()
        filter_1 = {"_id": document["_id"]}
        client['essme']['experts_vn'].replace_one(filter_1,document)
    except Exception:
        print(document["_id"], "error");
    