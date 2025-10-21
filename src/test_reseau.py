from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

URIS = [
    "mongodb://localhost:27020",  # routeur_1
    "mongodb://localhost:27021",  # routeur_2
]


def test_conn(uri):
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
        print(f"OK connexion {uri}")
    except ConnectionFailure:
        print(f"ECHEC connexion {uri}")


if __name__ == "__main__":
    for u in URIS:
        test_conn(u)
