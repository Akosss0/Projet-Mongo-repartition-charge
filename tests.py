from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import unittest

class TestMongo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = MongoClient("mongodb://principal_a:27017,principal_b:27017,principal_c:27017")
        cls.client.connect()

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

    def test_connexion(self):
        try:
            self.client.admin.command('ismaster')
        except ConnectionFailure as e:
            self.fail(f"Echec connexion à mongoDB : {e}")

    def test_total_documents(self):
        db = self.client["database"]
        collection = db["books"]

        self.assertEqual(collection.count_documents(),431)
    
    def test_nb_replicats(self):
        repl_status = self.client.admin.command("replSetGetStatus")
        self.assertEqual(len(repl_status["members"]),3)

    def test_nb_shards(self):
        shards = self.client.admin.command("listShards")
        self.assertEqual(len(shards['shards']),9)

    def test_synchro(self):
        db = self.client["database"]
        collection = db["books"]

        collection.insert_one({"name": "test", "value": 123})

        doc = collection.find_one({"name": "test"})
        self.assertIsNotNone(doc)
        self.assertEqual(doc["value"], 123)

        last_operations = []
        status = self.client.admin.command("replSetGetStatus")
        for member in status["members"]:
            last_operations.append(member['optime']['ts'])
        
        # Clean up
        collection.delete_one({"name": "test"})

        # On vérifie que la date est la même partout
        self.assertEqual(len(set(last_operations)),1)

    def test_secondaire(self):
        self.client = MongoClient("mongodb://principal_a:27017,principal_b:27017,principal_c:27017", read_preference="secondary")
        self.client.connect()
        db = self.client["database"]
        collection = db["books"]

        self.assertEqual(collection.count_documents(),431)


if __name__ == '__main__':
    unittest.main()