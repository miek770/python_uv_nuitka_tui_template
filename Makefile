NAME = $(shell grep '^name =' pyproject.toml | sed -E 's/name = "(.*)"/\1/')
VERSION = $(shell grep '^version =' pyproject.toml | sed -E 's/version = "(.*)"/\1/')

build:
	uv run python -m nuitka --onefile --show-progress --output-filename=$(NAME)_v$(VERSION).exe src/cli.py

info:
	@echo $(NAME), version $(VERSION)

tests:
	uv run python -m pytest

.PHONY: build info tests
