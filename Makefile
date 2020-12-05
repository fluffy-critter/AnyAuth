all: format pylint flake8

.PHONY: format
format:
	poetry run isort .
	poetry run autopep8 -r --in-place .

.PHONY: pylint
pylint:
	poetry run pylint app.py

.PHONY: flake8
flake8:
	poetry run flake8

