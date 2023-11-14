from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')
filter={'img': "https://test.cdn.culinarywonderland.com/photo/ne/news_image.jpg"}
sort=list({
    'created_date': -1
}.items())

result = client['essme']['news'].find(
  filter=filter,
  sort=sort
)

for document in result:
    try:
        document["img"] = "https://test.cdn.culinarywonderland.com/photo/se/news_default_2893743.jpg"
        filter_1 = {"_id": document["_id"]}
        client['essme']['news'].replace_one(filter_1,document)
    except Exception:
        print(document["_id"], "error");
    