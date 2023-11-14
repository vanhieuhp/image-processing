import random
import string
from pymongo import MongoClient
from unidecode import unidecode

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://admin:password@localhost:27017/?authMechanism=SCRAM-SHA-1')
filter = {
    'email': "Hanoi"
}

result = client['essme']['experts_vn'].find(
    filter=filter
)
arrays = []


def main():
    for document in result:
        try:

            email = document["display_name"]
            email = unidecode(email)
            email = email.lower().replace(" ", "") + generate_random_string(4) + "@gmail.com"
            print(email)
            arrays.append(email)
            document["email"] = email
            filter_1 = {"_id": document["_id"]}
            client['essme']['experts_vn'].replace_one(filter_1, document)
        except Exception:
            print(document["_id"], "error")

    duplicates = find_duplicates_using_sets(arrays)
    print("Duplicates:", duplicates)


def find_duplicates_using_sets(lst):
    unique_set = set()
    duplicates = []

    for item in lst:
        if item in unique_set:
            duplicates.append(item)
        else:
            unique_set.add(item)

    return duplicates


def generate_random_string(length):
    characters = string.digits  # Only digits (numbers)
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

main()
