dev:
	pip install -e ".[dev]"

lint:
	ruff check .

test:
	pytest ./tests

type:
	pyright validator

qa:
	make lint
	make type
	# TODO: re-enable this once we have the org environment set up
	# make test