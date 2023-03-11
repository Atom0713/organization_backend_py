# organization_backend_py

## Description 

Backend for Antalya Vandals Dashboard

## Manage dependecies
### Add dependency
 > poetry add [dependency-name]
 
 It will resolve and write the dependency, with it's requirements, to the `poetry.lock` file. 
 
 **Remember to commit `poetry.lock` to git.**

## Contribution

## Running locally
- Windows
1. Create virtual environemnt
    > python -m venv venv
2. Activate virtual environment: 
    > venv\Scripts\activate
3. Install dependency management tool called `poetry`
3. Install dependencies
    > poetry install
4. Start the application in the debug mode
    > flask --debug run

To deactivate virtual environement type `deactivate` in the Command Prompt

- Linux/macOS

## Testing
### Linting check:
- Windows.
> poetry run flake8
- Linux/macOS

### Typing check:
- Windows.
> poetry run mypy
- Linux/macOS

### Run tests:
- Windows.
> poetry run pytest
- Linux/macOS 
