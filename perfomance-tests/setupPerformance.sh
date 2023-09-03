#!/bin/bash

kubectl config set-context --current --namespace=luisa-parra

kubectl apply -f python-deployment.yaml