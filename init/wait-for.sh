#!/usr/bin/env bash
# petit helper pour attendre qu'un service docker soit joignable
# usage: wait-for.sh host port timeout
HOST=$1
PORT=$2
TIMEOUT=${3:-30}

n=0
until nc -z $HOST $PORT >/dev/null 2>&1
do
  n=$((n+1))
  if [ $n -ge $TIMEOUT ]; then
    echo "Timeout waiting for $HOST:$PORT" >&2
    exit 1
  fi
  sleep 1
done
exit 0