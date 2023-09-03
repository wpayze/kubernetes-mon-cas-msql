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

curl -L -o /tmp/data/brands.csv "https://www.dropbox.com/scl/fi/9p4qyhhm598knm87m0xm6/brands.csv?rlkey=bmtrp09580i5lloe4dcqntp83&dl=1"
curl -L -o /tmp/data/models.csv "https://www.dropbox.com/scl/fi/nwpo2t7jzv3ldiuc7ark4/models.csv?rlkey=kgcfhpemfo5a1kulq56ldkvpb&dl=1"
curl -L -o /tmp/data/owners.csv "https://www.dropbox.com/scl/fi/p496m1fde0llalxizwwpm/owners.csv?rlkey=jhh9nokxh9q3kz74yjej1axs0&dl=1"
curl -L -o /tmp/data/vehicle_owners.csv "https://www.dropbox.com/scl/fi/fit8oz9wds4j9ui9kqx1n/vehicle_owners.csv?rlkey=bni00y4ud9aiiskay5wla4qk0&dl=1"
curl -L -o /tmp/data/vehicles.csv "https://www.dropbox.com/scl/fi/1e2dwigc57489dpmyvf95/vehicles.csv?rlkey=2bh6eyx1oxjlskdni9drnx5dx&dl=1"

cqlsh -f /docker-entrypoint-setup.d/setup.cql