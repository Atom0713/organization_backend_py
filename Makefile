build:
	docker build --no-cache -t organization_py .

run:
	docker run -p 3000:3000 --rm organization_py