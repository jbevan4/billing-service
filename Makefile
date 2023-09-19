.PHONY: test test-with-coverage open-html-coverage lint format

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov --cov-report xml:coverage.xml --cov-report html:coverage-html --cov-fail-under=0

open-html-coverage:
	open htmlcov/index.html

lint:
	ruff . --fix

format:
	black .