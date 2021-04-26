from unittest import TestCase
from POC_mongo.mongo_connection import MongoConnection


class Evaluate(TestCase):
    def test_select_all(self):
        mongo = MongoConnection("mongodb", "test")
        actual = mongo.select_all()
        expected = 'None'
        self.assertEqual(expected, actual)

    def test_insert(self):
        mongo = MongoConnection("mongodb", "test")
        mongo.insert({'something': 'hello', 'number': 1})
        actual = mongo.select('number', 1)
        expected = {'something': 'hello', 'number': 1}
        self.assertEqual(expected, actual)

    def test_select(self):
        mongo = MongoConnection("mongodb", "test")
        actual = mongo.select_all()
        expected = 'None'
        self.assertEqual(expected, actual)

    def test_update(self):
        mongo = MongoConnection("mongodb", "test")
        actual = mongo.select_all()
        expected = 'None'
        self.assertEqual(expected, actual)

    def test_delete(self):
        mongo = MongoConnection("mongodb", "test")
        actual = mongo.select_all()
        expected = 'None'
        self.assertEqual(expected, actual)
