apply deployment:
kubectl apply -f deployment.yaml

get pods:
kubectl get pods

expose pod(because it's only inside the minikube):
kubectl expose deployment fast-api --type=NodePort --port=8000 --target-port=8000

get url of pod: 
minikube service fast-api --url

fetch.


ingress:
 ✗ minikube addons enable ingress   
 ✗ kubectl get pods -n ingress-nginx
 