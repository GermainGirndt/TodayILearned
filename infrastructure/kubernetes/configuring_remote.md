# Configuring remote on Kubernetes

- Pointing the kubernetes file to remote

### Install oidc login

OIDC stands for Open ID Connection.

For automatic Auth2.0 login, install kubectl oidc-login.

### Set the kube config file 

Download the kubeconfig file provided by your remote server and set it:

```
export KUBECONFIG="/Users/YOUR_USER/.kube/kubeconfig-kyma-saas.yaml"
```

### Use the config file context and desired namespace

```
kubectl config get-context

kubectl config use-context CONTEXT_HERE

kubectl get namespace

kubectl config set-context --curent --namespace=NAMESPACE_HERE
```
