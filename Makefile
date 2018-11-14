VERSION=$(shell date +%Y%m%d-%H%M)
NAME=choosecat
DC=docker-compose

all:

docker-test:
	$(DC) build && $(DC) run --rm local pytest

build:
	docker build -t $(NAME):$(VERSION) .

# ::::: Kubernetes

kexpose:
	kubectl expose deployment $(NAME) --type=LoadBalancer

kset-image: 
	kubectl set image deployment/$(NAME) \
	$(NAME)=$(NAME):$(VERSION)
kapply: build kset-image

krun:
	kubectl run $(NAME) --image=$(NAME):$(VERSION) \
	--port=8080 --image-pull-policy=Never

knukeall:
	kubectl delete deploy --all
