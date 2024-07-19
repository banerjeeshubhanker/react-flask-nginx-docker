from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient(os.environ.get('MONGO_URI', 'mongodb://admin:admin@mongo:27017/'))
db = client.helloworlddb
collection = db.messages

@app.route('/api/hello', methods=['GET'])
def hello_world():
    message = collection.find_one({"type": "greeting"})
    return jsonify(message=message['text'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
