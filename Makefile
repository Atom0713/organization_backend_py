network:
	docker network create organization_network

mysql:
	docker run -d \
		--network organization_network --network-alias mysql \
		-v organization_mysql_data:/var/lib/mysql \
		-e MYSQL_ROOT_PASSWORD=password \
		-e MYSQL_DATABASE=organizationdb \
		mysql:8.0
build:
	docker build --no-cache -t organization_py .

run: mysql
	docker run -p 3000:3000 --rm organization_py