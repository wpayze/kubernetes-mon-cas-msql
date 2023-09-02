#!/bin/bash

# Crear namespace
kubectl create namespace cassandra
kubectl config set-context --current --namespace=cassandra

# Crear ConfigMap para el script de inicialización
kubectl create configmap cassandra-init-script --from-file=initialize-db.sh
kubectl create configmap cassandra-setup-cql --from-file=setup.cql

# Crear Secret para almacenar las credenciales
kubectl create -f cassandra-secret.yaml

# Crear el Deployment de Cassandra
kubectl apply -f cassandra-deployment.yaml

# Mostrar el estado de los pods para confirmar que todo se ha creado correctamente
kubectl get pods --namespace=cassandra
