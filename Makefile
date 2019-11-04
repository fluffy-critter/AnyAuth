all: format pylint flake8

.PHONY: format
format:
	pipenv run isort -y
	pipenv run autopep8 -r --in-place .

.PHONY: pylint
pylint:
	pipenv run pylint app.py

.PHONY: flake8
flake8:
	pipenv run flake8

