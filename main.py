import pymongo

password = 'dvirko1221'
database = 'DB'
link = "mongodb+srv://dvir:" + password + "@data.my748.mongodb.net/" + database + "?retryWrites=true&w=majority"


def get_data():
    client = pymongo.MongoClient(link)
    db = client.get_database(database)
    col = db.get_collection('user')
    for doc in col.find():
        for value in doc.values():
            print(value)
    client.close()


get_data()
