from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)


class MongoConnection:
    def __init__(self, db_mongo, collection_mongo):
        self.db = db_mongo
        self.collection = collection_mongo

    def insert(self, document):
        db = client[self.db]
        collection = db[self.collection]
        collection.insert_one(document)

    def select(self,  select_by, value):
        db = client[self.db]
        collection = db[self.collection]
        info = collection.find_one({select_by: value})
        pprint.pprint(info)

    def update(self, number, new_number):
        db = client[self.db]
        collection = db[self.collection]
        old = {
            'number': number
        }
        new = {"$set": {
            'number': new_number
        }
        }
        collection.update_one(old, new)
        print("New value \n")
        self.select('number', new_number)

    def delete(self, number):
        db = client[self.db]
        collection = db[self.collection]
        collection.delete_one({'number': number})

    def select_all(self):
        res = []
        db = client[self.db]
        collection = db[self.collection]
        for info in collection.find():
            res.append(info)
            pprint.pprint(info)
        print("It works!", self.db, self.collection)
        return res


if __name__ == '__main__':
    mongo = MongoConnection("mongodb", "test")
    data = {'something': 'hello', 'number': 1}
    mongo.insert(data)
    mongo.select('something', 'hello')
    # mongo.select_all()
    mongo.delete(11)
    # mongo.select_all()
    # mongo.update(89, 90)
