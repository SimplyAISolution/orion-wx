.PHONY: run test lint format type

run:
	uvicorn src.api.main:app --reload --port 8000

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

type:
	mypy src
