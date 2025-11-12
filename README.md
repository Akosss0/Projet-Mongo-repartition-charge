# Projet-Mongo-repartition-charge
## `guide_installation.md`


## Prérequis
- Docker & Docker Compose
- Python 3.8+ et pip
- `pymongo` (pip install pymongo)

## Lancement
1. Démarrer les conteneurs :
   ```bash
   docker-compose up -d
   ```
2. Initialiser les replica sets des primaires (exécuter dans le conteneur correspondant) :
   ```bash
   docker exec -it principal_a mongosh --port 27017
   load('/init/init_shards.js')
   init_rsA()   # dans le prompt mongosh
   # répéter pour principal_b (init_rsB) et principal_c (init_rsC)
   ```
3. Initialiser le config server (peut être automatique si monté) :
   ```bash
   docker exec -it configsvr1 mongosh --port 27019
   load('/docker-entrypoint-initdb.d/init_configsvr.js')
   ```
4. Ajouter les shards via `mongos` (routeur) :
   ```bash
   # dans le container routeur_1
   docker exec -it routeur_1 bash -c "/init/init_mongos.sh 27020"
   # ou routeur_2 avec 27021
   ```
5. (Optionnel) lancer le historian en local ou dans un conteneur séparé :
   ```bash
   python src/historian.py
   ```

## Importer les données (ex. books.json)
- Via mongoimport :
  ```bash
  mongoimport --host localhost --port 27020 --db books --collection authors --file books.json --jsonArray
  ```
- Ou via le script Python :
  ```bash
  python src/init_data.py
  ```

## Tests
- Test de connectivité : `python src/test_reseau.py`
- Vérifier le sharding : dans `mongosh` sur `routeur_1` : `sh.status()`

## Arrêt et nettoyage
```bash
docker-compose down -v
```
