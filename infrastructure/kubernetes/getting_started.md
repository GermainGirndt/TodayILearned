### Minikube

Minikube is a docker containized Kubernetes for tests. Follow the install instructions on:

```
https://minikube.sigs.k8s.io/docs/start/
```

### Start

```
minikube start --driver=docker
```

### Checkup

kubectl is the containzed kubernetes instance CLI (using minikub)

```
kubectl get node
```

### Running

ConfigMap and Secrets muss exist before Deployments

- manages applycation through files defininign k8 resources

```
kubectl apply -f filename.yaml
```

### Infos

kubectl get all
kubectl get configmap
kubectl get secrets
kubectl describe service mongo-service
kubectl logs mongo-pod-name
