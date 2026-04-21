# Kubernetes CI/CD Demo with Helm, Ingress, and GitHub Actions

## Overview

This project demonstrates an end-to-end **containerized application deployment pipeline** using Kubernetes and Helm, fully automated with CI/CD.

It starts with a Dockerized FastAPI service, deploys it to Kubernetes using Helm, exposes it via Ingress, and automates deployments using GitHub Actions.

---

## Architecture

* **Application:** FastAPI (served with Uvicorn)
* **Containerization:** Docker (multi-arch build)
* **Orchestration:** Kubernetes
* **Packaging:** Helm
* **CI/CD:** GitHub Actions
* **Cluster (CI):** Kind (Kubernetes in Docker)

---

## Features

* Reusable Helm chart for deployments
* Ingress-based routing (L7 traffic management)
* Automated CI/CD pipeline
* Multi-architecture Docker builds (amd64 + arm64)
* Built-in debugging and observability in pipeline
* Ephemeral Kubernetes cluster for CI testing

---

## Project Structure

```
k8s-demo/
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── values.yaml
Dockerfile
.github/workflows/helm-ci-cd.yml
```

---

## How It Works

### 1. Build & Containerize

* FastAPI app is containerized using Docker
* Image supports both amd64 and arm64 architectures

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t <your-dockerhub>/k8s-demo-api:latest \
  --push .
```

---

### 2. Deploy with Helm

The Helm chart defines:

* Deployment (replicas, image, ports)
* Service (ClusterIP)
* Ingress (domain routing)

```bash
helm upgrade --install my-release ./k8s-demo \
  --namespace default \
  --create-namespace
```

---

### 3. CI/CD Pipeline

On every push:

* ✅ Helm lint
* ✅ Helm template validation
* 🚀 Deploy to Kubernetes cluster (Kind)

Workflow highlights:

```yaml
- uses: actions/checkout@v4
- uses: helm/kind-action@v1
- uses: azure/setup-helm@v4

- run: helm lint ./k8s-demo
- run: helm upgrade --install ...
```

---

## Debugging & Observability

The pipeline includes built-in debugging:

```bash
kubectl get all
kubectl describe pods
kubectl logs
```

This allows rapid troubleshooting of:

* CrashLoopBackOff
* Image pull errors
* Readiness/liveness failures
