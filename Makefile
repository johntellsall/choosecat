VERSION=$(shell date +%Y%m%d-%H%M)
NAME=choosecat

all:


	# eval $$(minikube docker-env) 
build:
	docker build -t $(NAME):$(VERSION) .
set-image: 
	kubectl set image deployment/$(NAME) \
	$(NAME)=$(NAME):$(VERSION)
apply: build set-image

run:
	kubectl run $(NAME) --image=$(NAME):$(VERSION) \
	--port=8080 --image-pull-policy=Never

nuke-everything:
	kubectl delete deploy --all
