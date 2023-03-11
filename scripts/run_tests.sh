#!/bin/bash
echo "Run linting check"
poetry run flake8 src tests


echo "Run typing check"
poetry run mypy src tests

echo "Run tests"
poetry run pytest
