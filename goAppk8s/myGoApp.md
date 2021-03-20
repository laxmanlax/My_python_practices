# This is a simple go-web-app appllication 



# Deploy go-web-app to a minikube cluster
I have added a Dockerfile and deployment.yaml file and steps needed to create this cluster 

1. docker build -t <username>/go-web-app .
2. docker push <username>/go-web-app:latest
3. minikube start
4. kubectl create -f deployment.yaml
5. kubectl expose deployment my-go-app --type=LoadBalancer --port=8080
6. minikube service my-go-app
