# organization_backend_py

## Description 

Backend for Antalya Vandals Dashboard

## Manage dependecies

## Contribution

## Running locally
To run service locally:
1. Create virtual environemnt: `python -m venv venv`
2. Activate virtual environment: `venv\Scripts\activate`(Windows)
3. Install dependencies: `poetry install`
4. Start application using:
    a. `scripts/run_dev_env.sh` script in bash 
    b. `flask --debug run` in CMD (windows)

`deactivate` to deactivate virtual environement.

## Testing
Use `scripts/run_tests.sh` to run linting, typing, and run tests.

### Add dependency:
 Run `poetry add [dependency-name]`. It will resolve and write the dependency, with it's requirements, to the `poetry.lock` file. 
 
 **Remember to commit `poetry.lock` to git.** 
