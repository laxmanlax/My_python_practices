FROM golang:1.15.7-buster
ENV SERVER_PORT=:8080
RUN go get -u github.com/gorilla/mux
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go build -o main .
CMD ["/app/main"]
#  docker run -p 8081:8080 -it laxman/go-web-app
#  https://minikube.sigs.k8s.io/docs/start/