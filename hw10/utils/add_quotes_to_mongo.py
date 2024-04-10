import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
db = client.db10

json_path = Path(__file__).resolve().parent / 'quotes.json'
with open(json_path, 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for qoute in quotes:
    author = db.authors.find_one({'fullname': qoute['author']})
    if author:
        db.quotes.insert_one({
            'quote': qoute['quote'],
            'tags': qoute['tags'],
            'author':ObjectId(author['_id'])
        })