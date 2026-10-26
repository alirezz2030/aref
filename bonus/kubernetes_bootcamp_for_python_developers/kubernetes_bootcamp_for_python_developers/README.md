# Kubernetes Bootcamp for Python Developers

## Included
- `kubernetes_bootcamp_for_python_developers.ipynb`: 30 lessons with detailed Markdown explanations and commented examples.
- `kubernetes_practice_project/`: Flask + Redis application, Dockerfile, and Kubernetes manifests for Namespace, ConfigMap, PVC, Deployments, Services, probes, HPA (optional), and ResourceQuota (optional).

## Quick start
1. Install Docker Desktop with Kubernetes, Minikube, or kind, plus `kubectl`.
2. Open a terminal in `kubernetes_practice_project/`.
3. Build: `docker build -t k8s-flask-redis:dev .`
4. If using kind: `kind load docker-image k8s-flask-redis:dev`; if using Minikube: `minikube image load k8s-flask-redis:dev`. For Docker Desktop, verify the selected cluster can see the local image.
5. Follow `kubernetes_practice_project/README.md` to apply manifests and test the service.

The project is for local learning. It is not a production-ready deployment, and deleting the namespace may delete the PVC and its data.
