#!/bin/bash
echo "Run linting check"
poetry run flake8


echo "Run typing check"
poetry run mypy

echo "Run tests"
poetry run pytest
