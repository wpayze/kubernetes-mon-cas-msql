#!/bin/sh

mkdir -p /tmp/data

curl -L -o /tmp/data/brands.csv "https://www.dropbox.com/scl/fi/mcxslsmo4keaiz8jhov5v/brands.csv?rlkey=4z8js0uqfknckhijaqkpn9x6h&dl=1"
curl -L -o /tmp/data/models.csv "https://www.dropbox.com/scl/fi/pe3guzvx9w8tps7gp9qu7/models.csv?rlkey=lftqzh47qckhx53ttc4u79pvf&dl=1"
curl -L -o /tmp/data/owners.csv "https://www.dropbox.com/scl/fi/lgm7hc3yhx4za3f43d3xt/owners.csv?rlkey=yqwl0zk3chkly6razz1zy1jb5&dl=1"
curl -L -o /tmp/data/vehicle_owners.csv "https://www.dropbox.com/scl/fi/pg1mfe32x0ymbxnxks8r3/vehicle_owners.csv?rlkey=px9gev124onudq4ptd8y6gtd6&dl=1"
curl -L -o /tmp/data/vehicles.csv "https://www.dropbox.com/scl/fi/tvasqr50zg40fsn8q1h3k/vehicles.csv?rlkey=3pxrf0d0hv2jpy71uognsunir&dl=1"

until mysqladmin ping --host=localhost --user=root --password=$MYSQL_ROOT_PASSWORD; do
    echo --password=$MYSQL_ROOT_PASSWORD;
    sleep 2
done

# Ahora, ejecuta setup.sql:
# sed -i "s/'hereisthepassword'/'$MYSQL_ROOT_PASSWORD'/g" /docker-entrypoint-setup.d/setup.sql
mysql -h localhost --local-infile=1 -u root --password=$MYSQL_ROOT_PASSWORD < /docker-entrypoint-setup.d/setup.sql