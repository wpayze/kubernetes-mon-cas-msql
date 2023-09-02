-- Crear el keyspace si no existe
CREATE KEYSPACE IF NOT EXISTS cassandra_vehicles WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

-- Usar el keyspace
USE cassandra_vehicles;

-- Creación de la tabla brands
DROP TABLE IF EXISTS brands;

CREATE TABLE IF NOT EXISTS brands (
    brand_ID UUID PRIMARY KEY,
    name TEXT
);

-- Creación de la tabla models
DROP TABLE IF EXISTS models;

CREATE TABLE IF NOT EXISTS models (
    model_ID UUID PRIMARY KEY,
    name TEXT,
    brand_id UUID
);

-- Creación de la tabla owners
DROP TABLE IF EXISTS owners;

CREATE TABLE IF NOT EXISTS owners (
    owner_ID UUID PRIMARY KEY,
    name TEXT,
    contact_info TEXT
);

-- Creación de la tabla vehicles
DROP TABLE IF EXISTS vehicles;

CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_ID UUID PRIMARY KEY,
    model_id UUID,
    year INT,
    color TEXT
);

-- Creación de la tabla vehicle_owners
DROP TABLE IF EXISTS vehicle_owners;

CREATE TABLE IF NOT EXISTS vehicle_owners (
    id UUID PRIMARY KEY,
    vehicle_id UUID,
    owner_id UUID,
    purchase_date DATE
);

-- Importar CSV a Cassandra. Estas rutas deben ser accesibles por cqlsh
COPY brands(brand_ID, name) FROM '/tmp/data/brands.csv' WITH DELIMITER = ',' AND HEADER = TRUE;
COPY models(model_ID, name, brand_id) FROM '/tmp/data/models.csv' WITH DELIMITER = ',' AND HEADER = TRUE;
COPY owners(owner_ID, name, contact_info) FROM '/tmp/data/owners.csv' WITH DELIMITER = ',' AND HEADER = TRUE;
COPY vehicles(vehicle_ID, model_id, year, color) FROM '/tmp/data/vehicles.csv' WITH DELIMITER = ',' AND HEADER = TRUE;
COPY vehicle_owners(id, vehicle_id, owner_id, purchase_date) FROM '/tmp/data/vehicle_owners.csv' WITH DELIMITER = ',' AND HEADER = TRUE;
