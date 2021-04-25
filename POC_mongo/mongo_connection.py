from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)


class MongoConnection:
    def __init__(self, db_mongo, collection_mongo):
        self.db = db_mongo
        self.collection = collection_mongo

    def insert(self, document):
        self.collection.insert_one(document)

    def select(self, number):
        info = self.collection.find_one({'number': number})
        pprint.pprint(info)

    def update(self, number, new_number):
        old = {
            'number': number
        }
        new = {"$set": {
            'number': new_number
        }
        }
        self.collection.update_one(old, new)
        print("New value \n")
        self.select(new_number)

    def delete(self, number):
        self.collection.delete_one({'number': number})

    def select_all(self):
        # for info in collection.find():
        #   pprint.pprint(info)
        print("It works!", self.db, self.collection)
        return 'None'


if __name__ == '__main__':
    mongo = MongoConnection("mongodb", "test")
    # mongo.insert({'number': 10})
    mongo.select_all()
    # mongo.update(89, 90)
