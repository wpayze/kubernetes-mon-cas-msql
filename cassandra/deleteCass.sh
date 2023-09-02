#!/bin/bash

# Eliminar el Deployment de Cassandra
kubectl delete -f cassandra-deployment.yaml

# Eliminar Secret
kubectl delete secret cassandra-secret

# Eliminar ConfigMap
kubectl delete configmap cassandra-init-script
kubectl delete configmap cassandra-setup-cql

# Cambiar el contexto al namespace por defecto
kubectl config set-context --current --namespace=default

# Mostrar el estado de los pods en el namespace por defecto para confirmar que todo se ha eliminado
kubectl get pods --namespace=cassandra
