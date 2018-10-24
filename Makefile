all:

VERSION=$(shell date +%Y%m%d-%H%M)
NAME=choosecat

	# eval $$(minikube docker-env) 
build:
	docker build -t $(NAME):$(VERSION) .
apply: 
	kubectl set image deployment/$(NAME) \
	$(NAME)=$(NAME):$(VERSION)
