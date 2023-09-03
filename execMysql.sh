#!/bin/bash

kubectl create namespace luisa-parra
kubectl config set-context --current --namespace=luisa-parra

kubectl create configmap mysql-scripts --from-file=initialize-db.sh=./initialize-db.sh
kubectl create configmap mysql-setup  --from-file=setup.sql=./setup.sql

# Aplicar los archivos de configuración en orden adecuado
# kubectl apply -f mysql-pv-pvc.yaml
kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f mysql-service.yaml

kubectl apply -f sysbench-deployment.yaml

# Mostrar el estado de los pods para confirmar que todo se ha creado correctamente
kubectl get pods --namespace luisa-parra