
deps:
	@pip install -r requirements.txt

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
	@python manage.py test --settings kamboard.settings_test --verbosity=2

coverage: clean
	coverage run --source='.' manage.py test --settings kamboard.settings_test && coverage html && coverage report

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
