<?php
ini_set('memory_limit', '8G');
require 'vendor/autoload.php';
use Faker\Factory;
use Ramsey\Uuid\Uuid;
set_time_limit(300);

$faker = Factory::create();

// 3 Millones
// $brandsCount = 15000;
// $modelsPerBrand = 5;
// $vehiclesCount = 3000000;
// $ownersCount = 2100000;

// 1 Millon
$brandsCount = 5000;
$modelsPerBrand = 5;
$vehiclesCount = 1000000;
$ownersCount = 700000;

// Cien
// $brandsCount = 10;
// $modelsPerBrand = 2;
// $vehiclesCount = 100;
// $ownersCount = 70;

$brands = [];
$models = [];
$vehicles = [];
$owners = [];
$vehicleOwners = [];

for ($i = 0; $i <= $brandsCount; $i++) {
    $brands[] = [
        'brand_ID' => Uuid::uuid4()->toString(),
        'name' => $faker->company,
    ];
}

for ($i = 0; $i < $brandsCount; $i++) {
    for ($j = 0; $j < $modelsPerBrand; $j++) {
        $models[] = [
            'model_ID' => Uuid::uuid4()->toString(),
            'name' => $faker->word,
            'brand_id' => $brands[$i]['brand_ID'],
        ];
    }
}

for ($i = 0; $i <= $vehiclesCount; $i++) {
    $vehicles[] = [
        'vehicle_ID' => Uuid::uuid4()->toString(),
        'model_id' => $models[$faker->numberBetween(0, count($models) - 1)]['model_ID'],
        'year' => $faker->year,
        'color' => $faker->safeColorName,
    ];
}

for ($i = 0; $i <= $ownersCount; $i++) {
    $owners[] = [
        'owner_ID' => Uuid::uuid4()->toString(),
        'name' => $faker->name,
        'contact_info' => $faker->email,
    ];
}

for ($i = 0; $i <= $vehiclesCount; $i++) {
    $vehicleOwners[] = [
        'id' => Uuid::uuid4()->toString(),
        'vehicle_id' => $vehicles[$i]['vehicle_ID'],
        'owner_id' => $owners[$faker->numberBetween(0, count($owners) - 1)]['owner_ID'],
        'purchase_date' => $faker->dateTimeBetween('-10 years', 'now')->format('Y-m-d'),
    ];
}

$csvPath = 'csv_files/';
if (!is_dir($csvPath)) {
    mkdir($csvPath);
}

function exportToCSV($data, $fileName) {
    global $csvPath;
    $filePath = $csvPath . $fileName;
    $fp = fopen($filePath, 'w');
    fputcsv($fp, array_keys($data[0])); 
    foreach ($data as $row) {
        fputcsv($fp, $row);
    }
    fclose($fp);
}

exportToCSV($brands, 'brands.csv');
exportToCSV($models, 'models.csv');
exportToCSV($vehicles, 'vehicles.csv');
exportToCSV($owners, 'owners.csv');
exportToCSV($vehicleOwners, 'vehicle_owners.csv');

echo "Archivos CSV generados exitosamente.";
