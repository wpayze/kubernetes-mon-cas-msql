SET
    GLOBAL local_infile = 1;

ALTER USER 'root'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'mysqlpass123';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS mysql_vehicles;

USE mysql_vehicles;

-- Creación de la tabla brands
DROP TABLE IF EXISTS brands;

CREATE TABLE brands (
    brand_ID CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Creación de la tabla models
DROP TABLE IF EXISTS models;

CREATE TABLE models (
    model_ID CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand_id CHAR(36),
    FOREIGN KEY (brand_id) REFERENCES brands(brand_ID)
);

-- Creación de la tabla owners
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    owner_ID CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255) NOT NULL
);

-- Creación de la tabla vehicles
DROP TABLE IF EXISTS vehicles;

CREATE TABLE vehicles (
    vehicle_ID CHAR(36) PRIMARY KEY,
    model_id CHAR(36),
    year INT,
    color VARCHAR(50),
    FOREIGN KEY (model_id) REFERENCES models(model_ID)
);

-- Creación de la tabla vehicle_owners
DROP TABLE IF EXISTS vehicle_owners;

CREATE TABLE vehicle_owners (
    id CHAR(36) PRIMARY KEY,
    vehicle_id CHAR(36),
    owner_id CHAR(36),
    purchase_date DATE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_ID),
    FOREIGN KEY (owner_id) REFERENCES owners(owner_ID)
);

-- Importar CSV a MySQL
-- LOAD DATA LOCAL INFILE '/csv/brands.csv' INTO TABLE brands FIELDS TERMINATED BY ',' IGNORE 1 LINES;

-- LOAD DATA LOCAL INFILE '/csv/models.csv' INTO TABLE models FIELDS TERMINATED BY ',' IGNORE 1 LINES;

-- LOAD DATA LOCAL INFILE '/csv/owners.csv' INTO TABLE owners FIELDS TERMINATED BY ',' IGNORE 1 LINES;

-- LOAD DATA LOCAL INFILE '/csv/vehicles.csv' INTO TABLE vehicles FIELDS TERMINATED BY ',' IGNORE 1 LINES;

-- SET
--     SESSION sql_mode = '';

-- LOAD DATA LOCAL INFILE '/csv/vehicle_owners.csv' INTO TABLE vehicle_owners FIELDS TERMINATED BY ',' IGNORE 1 LINES (id, vehicle_id, owner_id, @purchase_date)
-- SET
--     purchase_date = STR_TO_DATE(@purchase_date, '%c/%e/%Y');