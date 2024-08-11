# SPDX-License-Identifier: MIT
# Makefile

# Define the default shell
SHELL := /bin/bash

# Define the commands.
test:
	@poetry run pytest .

coverage:
	@coverage run -m pytest .
	@coverage report -m > coverage.txt

install:
	@poetry install --sync --no-interaction

build:
	@poetry build --verbose --no-interaction