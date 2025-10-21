#!/bin/bash
set -e
# Ce script est monté dans les containers routeur_* et permet d'exécuter addShard une fois que mongos est prêt.

MONGOS_PORT=${1:-27020}
MONGOSH_CMD="mongosh --port $MONGOS_PORT --eval"

# retry helper
retry(){
  n=0
  until [ $n -ge 30 ]
  do
    "$@" && break
    n=$((n+1))
    sleep 2
  done
}

# Add the three shards via mongos
echo "Waiting for mongos to be available on port $MONGOS_PORT..."
retry bash -c "${MONGOSH_CMD} 'db.adminCommand({ ping: 1 })'"

echo "Adding shards to cluster via mongos:$MONGOS_PORT"
${MONGOSH_CMD} "sh.addShard('rsA/principal_a:27017')"
${MONGOSH_CMD} "sh.addShard('rsB/principal_b:27017')"
${MONGOSH_CMD} "sh.addShard('rsC/principal_c:27017')"

# Enable sharding for example DB 'books'
${MONGOSH_CMD} "sh.enableSharding('books')"
# Example: shard the collection books.authors by 'author' field (hash or range as desired)
${MONGOSH_CMD} "sh.shardCollection('books.authors', { author: 1 })"

echo "Sharding configuré."