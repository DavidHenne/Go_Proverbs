build:
	docker-compose build

start-services:
	docker-compose up -d db

run:
	docker-compose run --rm --service-ports app

bash:
	docker exec -it $(cid) bash
