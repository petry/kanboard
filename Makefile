
deps:
	@pip install -r requirements.txt
	@pip install -r requirements_test.txt

migrate:
	@python manage.py migrate --settings kanboard.settings_local
	@python manage.py loaddata kanboard/fixtures/initial_data.json  --settings=kanboard.settings_local

setup: deps migrate

clean:
	@find . -name "*.pyc" -delete

run: clean
	@python manage.py runserver 0.0.0.0:8000 --settings kanboard.settings_local

test: clean
	@py.test

coverage: clean
	@py.test --cov . --cov-report html

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'

deploy:
	@git push heroku master
	@heroku run python manage.py migrate
