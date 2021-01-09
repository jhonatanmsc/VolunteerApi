.SILENT:

build:
	docker-compose build

up:
	docker-compose up

startup:
	docker-compose up --build

makemigrations:
	docker exec -it checkorders alembic revision --autogenerate -m "$(commit)"

migrate:
	docker exec -it checkorders alembic upgrade head