
deps:
	@pip install -r requirements.txt
	@pip install -r requirements_test.txt

migrate:
	@python manage.py syncdb --settings kamboard.settings_local
	@python manage.py migrate --settings kamboard.settings_local
	@python manage.py loaddata kamboard/fixtures/initial_data.json  --settings=kamboard.settings_local

setup: deps migrate

clean:
	@find . -name "*.pyc" -delete

run: clean
	@python manage.py runserver 0.0.0.0:8000 --settings kamboard.settings_local

test: clean
	@py.test

coverage: clean
	@py.test --cov . --cov-report html

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
