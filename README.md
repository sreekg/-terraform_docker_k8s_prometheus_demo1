# Terraform + Docker + Kubernetes (AKS) + Prometheus Demo

This repo provides a ready-to-run example that provisions Azure infra with Terraform,
builds and pushes a Dockerized Flask app to ACR, deploys to AKS, and installs
Prometheus/Grafana for monitoring.

## Quick start (local)

1. Provision infra (example):

   cd terraform
   terraform init
   terraform apply -auto-approve

2. Build & push Docker image (local):

   ACR_NAME=<<yourACRName>>
   az acr login --name $ACR_NAME
   docker build -t $ACR_NAME.azurecr.io/flask:1.0.0 -f app/Dockerfile app/
   docker push $ACR_NAME.azurecr.io/flask:1.0.0

3. Deploy to AKS (local):

   az aks get-credentials --resource-group <rg> --name <aks-name>
   kubectl apply -f k8s/namespace.yaml
   sed 's|REPLACE_WITH_IMAGE|<acr>.azurecr.io/flask:1.0.0|' k8s/deployment.yaml | kubectl apply -f -
   kubectl apply -f k8s/service.yaml

4. Install Prometheus & Grafana (via Helm):

   kubectl create namespace monitoring || true
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   helm upgrade --install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --values terraform/prom-values.yaml

## Notes
- Update pipeline service connection names before running in Azure DevOps.
- Use remote state for Terraform in production (Azure Storage + locking).
