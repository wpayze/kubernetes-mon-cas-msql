#!/bin/bash

# Eliminar los recursos en el orden correcto
kubectl delete -f mysql-service.yaml
kubectl delete -f mysql-deployment.yaml
kubectl delete configmap mysql-scripts
kubectl delete configmap mysql-setup
kubectl delete -f mysql-secret.yaml
kubectl delete -f mysql-pv-pvc.yaml

kubectl delete -f sysbench-deployment.yaml

# Cambiar el contexto al namespace por defecto
kubectl config set-context --current --namespace=default

# Mostrar el estado de los pods para confirmar que todo se ha eliminado correctamente
kubectl get pods --namespace mysql