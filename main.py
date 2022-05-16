import pymongo
from bson import json_util
import json
from bson import ObjectId
from password import *
from flask import *

app = Flask(__name__)
client = pymongo.MongoClient(link)
db = client.get_database(database)
col = db.get_collection('user')


@app.route('/')
def get_data():
    for doc in col.find():
        for value in doc.values():
            print(value)
    return jsonify([doc for doc in col.find()])


@app.route('/add/<name>', methods=['POST', 'GET'])
def post_data(name):
    add = {"name": name}
    col.insert_one(add)
    return 'add ' + name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
