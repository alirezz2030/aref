# Kubernetes Practice Project — Flask + Redis

This is a local learning app with two web replicas and a Redis service.

## Requirements
- Docker Desktop with Kubernetes enabled, Minikube, or kind.
- `kubectl`.
- A cluster with a default StorageClass for the Redis PVC.
- Build the image with Docker before applying the manifests.

## 1. Build the image
Run these commands from this directory:

```bash
docker build -t k8s-flask-redis:dev .
```

For **kind**, load the locally built image into the cluster:

```bash
kind load docker-image k8s-flask-redis:dev
```

For **Minikube**, use:

```bash
minikube image load k8s-flask-redis:dev
```

Docker Desktop's Kubernetes cluster can usually use the local Docker image directly, depending on the Docker Desktop/Kubernetes setup.

## 2. Validate and apply manifests
```bash
kubectl apply --dry-run=client -f k8s/00-namespace.yaml
kubectl apply -f k8s/00-namespace.yaml
kubectl apply -f k8s/01-configmap.yaml
kubectl apply -f k8s/02-redis-pvc.yaml
kubectl apply -f k8s/03-redis.yaml
kubectl apply -f k8s/04-web.yaml
```

Wait and inspect:

```bash
kubectl -n k8s-learning get pods,deployments,services,pvc
kubectl -n k8s-learning rollout status deployment/redis
kubectl -n k8s-learning rollout status deployment/web
kubectl -n k8s-learning logs deployment/web
```

## 3. Test the app
Open a second terminal and run:

```bash
kubectl -n k8s-learning port-forward service/web 8080:80
```

Visit `http://localhost:8080/`, `/health`, `/ready`, and `/visits`.

## 4. Scale and inspect
```bash
kubectl -n k8s-learning scale deployment/web --replicas=3
kubectl -n k8s-learning get pods -o wide
kubectl -n k8s-learning describe deployment web
```

The optional HPA manifest needs a functioning metrics API (often metrics-server):

```bash
kubectl apply -f k8s/05-hpa-optional.yaml
kubectl -n k8s-learning get hpa
```

## 5. Clean up
```bash
kubectl delete namespace k8s-learning
```

Deleting the namespace also deletes its resources, including the PVC. Depending on the storage class and PV reclaim policy, underlying storage behavior differs. Only run cleanup after confirming the namespace contains disposable learning resources.

## Important
This project is for local training, not production deployment. It uses a basic Redis setup without authentication and does not include TLS, production secrets management, network policies, a full monitoring stack, or backups.
