## Distributed Load Testing with Locust and Kubernetes
This repo contains the code for the blog post [Distributed Load Testing with Locust and Kubernetes](https://abmounir.com/posts/Distributed-load-testing-on-Kubernetes-with-Locust/)

### Add Delivery Hero public chart repo:

```bash
helm repo add deliveryhero "https://charts.deliveryhero.io/"
helm repo update deliveryhero
# Check
helm repo list | egrep "NAME|deliveryhero"
```

### Create configmap for locustfile.py
```bash
kubectl create configmap locust-config --from-file=locustfile.py
```
### Install Locust
```bash
helm upgrade --install locust deliveryhero/locust \
 --set loadtest.name=loadtest \
 --set loadtest.locust_locustfile_configmap=locust-config \
 --set loadtest.locust_locustfile=locustfile.py \
 --set worker.hpa.enabled=true \
 --set worker.hpa.minReplicas=5 

 ```
