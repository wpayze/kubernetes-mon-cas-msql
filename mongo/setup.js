const { MongoClient } = require('mongodb');

async function main() {
    const uri = 'mongodb://root:mongopass123@localhost:27017';
    const client = new MongoClient(uri);

    try {
        await client.connect();

        const mongo_vehicles = client.db('mongo_vehicles');

        await mongo_vehicles.createCollection('brands', {
            validator: {
                $jsonSchema: {
                    bsonType: 'object',
                    required: ['brand_ID', 'name'],
                    properties: {
                        brand_ID: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        name: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        }
                    }
                }
            }
        });

        await mongo_vehicles.createCollection('models', {
            validator: {
                $jsonSchema: {
                    bsonType: 'object',
                    required: ['model_ID', 'name', 'brand_id'],
                    properties: {
                        model_ID: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        name: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        brand_id: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        }
                    }
                }
            }
        });

        await mongo_vehicles.createCollection('owners', {
            validator: {
                $jsonSchema: {
                    bsonType: 'object',
                    required: ['owner_ID', 'name', 'contact_info'],
                    properties: {
                        owner_ID: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        name: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        contact_info: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        }
                    }
                }
            }
        });

        await mongo_vehicles.createCollection('vehicles', {
            validator: {
                $jsonSchema: {
                    bsonType: 'object',
                    required: ['vehicle_ID', 'model_id', 'year', 'color'],
                    properties: {
                        vehicle_ID: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        model_id: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        year: {
                            bsonType: 'int',
                            description: 'must be an integer and is required'
                        },
                        color: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        }
                    }
                }
            }
        });

        await mongo_vehicles.createCollection('vehicle_owners', {
            validator: {
                $jsonSchema: {
                    bsonType: 'object',
                    required: ['id', 'vehicle_id', 'owner_id', 'purchase_date'],
                    properties: {
                        id: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        vehicle_id: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        owner_id: {
                            bsonType: 'string',
                            description: 'must be a string and is required'
                        },
                        purchase_date: {
                            bsonType: 'date',
                            description: 'must be a date and is required'
                        }
                    }
                }
            }
        });

        console.log('Colecciones creadas con éxito.');

    } catch (err) {
        console.error(err);
    } finally {
        await client.close();
    }
}

main().catch(console.error);
