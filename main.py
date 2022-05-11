import pymongo
from password import *
from flask import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def get_data():
    client = pymongo.MongoClient(link)
    db = client.get_database(database)
    col = db.get_collection('user')
    for doc in col.find():
        for value in doc.values():
            print(value)
    client.close()
    return 'all_users'


@app.route('/add/<name>', methods=['POST', 'GET'])
def post_data(name):
    client = pymongo.MongoClient(link)
    db = client.get_database(database)
    col = db.get_collection('user')
    add = {"name": name}
    col.insert_one(add)
    client.close()

    return 'add '+name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
