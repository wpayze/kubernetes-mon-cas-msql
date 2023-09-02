#!/bin/bash
set -e

# Esperar a que Cassandra esté listo
while true; do
  if cqlsh -e 'describe cluster'; then
    break
  fi
  echo "Esperando a que Cassandra esté listo..."
  sleep 5
done

mkdir -p /tmp/data

curl -L -o /tmp/data/brands.csv "https://www.dropbox.com/scl/fi/5ais2btoa97dwguaedf3o/brands.csv?rlkey=0vmy8o1i94inig4uz4yo1s8s5&dl=1"
curl -L -o /tmp/data/models.csv "https://www.dropbox.com/scl/fi/52g4piqal2jt3h30e6gxi/models.csv?rlkey=4aua2zm716odn5mpr1hyxcid1&dl=1"
curl -L -o /tmp/data/owners.csv "https://www.dropbox.com/scl/fi/k5j59q55jmte8tc023u7b/owners.csv?rlkey=d616vpjj7k23bi5cmmi39zknb&dl=1"
curl -L -o /tmp/data/vehicle_owners.csv "https://www.dropbox.com/scl/fi/0dvm1og5kzphe7w8dg8zy/vehicle_owners.csv?rlkey=e0j2qosucfvoyvkvqnfd45lkj&dl=1"
curl -L -o /tmp/data/vehicles.csv "https://www.dropbox.com/scl/fi/3dyznncu1kl8waux4qrth/vehicles.csv?rlkey=w8mjqvdkex8315dokikvtwo6p&dl=1"

cqlsh -f /docker-entrypoint-setup.d/setup.cql