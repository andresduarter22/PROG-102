from unittest import TestCase
from POC_mongo.mongo_connection import MongoConnection


class Evaluate(TestCase):
    def test_select_all(self):
        mongo = MongoConnection("mongodb", "test")
        actual = mongo.select_all()
        expected = 'None'
        self.assertEqual(expected, actual)
