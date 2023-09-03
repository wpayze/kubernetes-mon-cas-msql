#!/bin/sh

mkdir -p /tmp/data

# Descargar archivos CSV
curl -L -o /tmp/data/brands.csv "https://www.dropbox.com/scl/fi/mcxslsmo4keaiz8jhov5v/brands.csv?rlkey=4z8js0uqfknckhijaqkpn9x6h&dl=1"
curl -L -o /tmp/data/models.csv "https://www.dropbox.com/scl/fi/pe3guzvx9w8tps7gp9qu7/models.csv?rlkey=lftqzh47qckhx53ttc4u79pvf&dl=1"
curl -L -o /tmp/data/owners.csv "https://www.dropbox.com/scl/fi/lgm7hc3yhx4za3f43d3xt/owners.csv?rlkey=yqwl0zk3chkly6razz1zy1jb5&dl=1"
curl -L -o /tmp/data/vehicle_owners.csv "https://www.dropbox.com/scl/fi/pg1mfe32x0ymbxnxks8r3/vehicle_owners.csv?rlkey=px9gev124onudq4ptd8y6gtd6&dl=1"
curl -L -o /tmp/data/vehicles.csv "https://www.dropbox.com/scl/fi/tvasqr50zg40fsn8q1h3k/vehicles.csv?rlkey=3pxrf0d0hv2jpy71uognsunir&dl=1"

# Espera hasta que MongoDB esté disponible
until nc -z localhost 27017; do
    echo "Waiting for MongoDB..."
    sleep 2
done

# Crear la base de datos y las colecciones
mongo --username=root --password=$MONGODB_ROOT_PASSWORD --eval 'db = db.getSiblingDB("mongo_vehicles"); db.createCollection("brands"); db.createCollection("models"); db.createCollection("owners"); db.createCollection("vehicles"); db.createCollection("vehicle_owners");'

# Importar datos desde archivos CSV
mongoimport --host=localhost --username=root --password=$MONGODB_ROOT_PASSWORD --db=mongo_vehicles --collection=brands --type=csv --file=/tmp/data/brands.csv --headerline
mongoimport --host=localhost --username=root --password=$MONGODB_ROOT_PASSWORD --db=mongo_vehicles --collection=models --type=csv --file=/tmp/data/models.csv --headerline
mongoimport --host=localhost --username=root --password=$MONGODB_ROOT_PASSWORD --db=mongo_vehicles --collection=owners --type=csv --file=/tmp/data/owners.csv --headerline
mongoimport --host=localhost --username=root --password=$MONGODB_ROOT_PASSWORD --db=mongo_vehicles --collection=vehicles --type=csv --file=/tmp/data/vehicles.csv --headerline
mongoimport --host=localhost --username=root --password=$MONGODB_ROOT_PASSWORD --db=mongo_vehicles --collection=vehicle_owners --type=csv --file=/tmp/data/vehicle_owners.csv --headerline
