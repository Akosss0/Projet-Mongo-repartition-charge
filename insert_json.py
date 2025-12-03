import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, BulkWriteError

def insert_json():
    """
    Insère books.json dans la base de données.
    La BD se nomme 'database'
    La collection se nomme 'books'
    """

    # Lit le fichier json
    with open('./books.json', 'r') as file:
        documents = json.load(file)

    # Se connecte à mongoDB avec un réplicat
    client = MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")

    try:
        # Vérifie la connexion
        client.admin.command('ismaster')
        print("Connexion réussie")

        # Créé et accède à la bd et à la collection
        db = client['database']
        collection = db['books']

        # Insert les documents
        result = collection.insert_many(documents)
        print(f"{len(result.inserted_ids)} documents insérés dans database.books")

    except ConnectionFailure as e:
        print(f"Echec de la connexion à la base : {e}")
    except BulkWriteError as e:
        print(f"Echec à l'insertion des documents : {e.details}")
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        client.close()

if __name__ == "__main__":
    insert_json()
