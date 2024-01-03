network:
	docker network create organization_network

mysql_init:
	docker run -d --rm\
		--network organization_network --network-alias mysql \
		-v organization_mysql_data:/var/lib/mysql \
		-e MYSQL_ROOT_PASSWORD=password \
		-e MYSQL_DATABASE=organizationdb \
		mysql:8.0
build:
	docker build -t organization_py .

run: mysql_init
	docker run -p 8080:5000 --rm --network organization_network organization_py

mysql_container ?= $(shell bash -c 'read -p "mysql container id: " username; echo $$mysql_container')


.PHONY: mysql
mysql:
	docker exec -it $(c) mysql -u root -p