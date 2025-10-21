# Script d'exemple pour insérer la base 'books' via pymongo en passant par un mongos
from pymongo import MongoClient
import json

MONGOS_URI = "mongodb://localhost:27020"


def import_books(json_file, db_name="books", coll_name="authors"):
    client = MongoClient(MONGOS_URI)
    db = client[db_name]
    coll = db[coll_name]
    with open(json_file, "r", encoding="utf-8") as f:
        docs = json.load(f)
        if isinstance(docs, list):
            coll.insert_many(docs)
        else:
            # si fichier json ligne par ligne
            f.seek(0)
            to_insert = []
            for line in f:
                line = line.strip()
                if not line:
                    continue
                to_insert.append(json.loads(line))
            if to_insert:
                coll.insert_many(to_insert)
    print("Import terminé.")


if __name__ == "__main__":
    import_books("books.json")
