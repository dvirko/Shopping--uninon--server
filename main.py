import pymongo
from password import *
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_data():
    client = pymongo.MongoClient(link)
    db = client.get_database(database)
    col = db.get_collection('user')
    for doc in col.find():
        for value in doc.values():
            print(value)
    client.close()

    return 'all users'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

