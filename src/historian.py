# historian.py
# Ce script se connecte au cluster via un mongos et écoute les change streams
# pour écrire une copie des changements dans la base 'historique' (sur le service 'historique').

from pymongo import MongoClient
from pymongo.errors import PyMongoError
import threading
import time

MONGOS_URI = "mongodb://localhost:27020"
HISTORIQUE_URI = (
    "mongodb://localhost:27017"  # si historique tourne sur 27017 local mapping
)

# NOTE: selon la façon dont docker mappe les ports, tu devras adapter les URI.


def watch_changes():
    client = MongoClient(MONGOS_URI)
    hist_client = MongoClient(HISTORIQUE_URI)
    hist_db = hist_client["historique_db"]
    hist_coll = hist_db["changelog"]

    # Watch all dbs and collections
    try:
        with client.watch(full_document="updateLookup") as stream:
            print("Historian: change stream ouvert...")
            for change in stream:
                # Enregistrer dans le serveur historique
                rec = {
                    "cluster_time": change.get("_id"),
                    "operationType": change.get("operationType"),
                    "ns": change.get("ns"),
                    "fullDocument": change.get("fullDocument"),
                    "documentKey": change.get("documentKey"),
                }
                hist_coll.insert_one(rec)
                print("Historian: écrit un changement", rec["operationType"])
    except PyMongoError as e:
        print("Historian erreur:", e)
        time.sleep(5)
        watch_changes()


if __name__ == "__main__":
    watch_changes()
