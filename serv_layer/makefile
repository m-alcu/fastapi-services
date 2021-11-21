install:
	pipenv install

build:
	docker-compose build

run:
	docker-compose up 

stop:
	docker-compose stop 

destroy:
	docker-compose down 

makemigrations:
	docker-compose run server alembic revision --autogenerate

migrate:
	docker-compose run server alembic upgrade head

shell:
	docker-compose run server bash 

python:
	docker-compose run server ipython
