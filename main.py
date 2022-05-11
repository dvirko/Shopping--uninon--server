import pymongo
from password import *


def get_data():
    client = pymongo.MongoClient(link)
    db = client.get_database(database)
    col = db.get_collection('user')
    for doc in col.find():
        for value in doc.values():
            print(value)
    client.close()


get_data()
