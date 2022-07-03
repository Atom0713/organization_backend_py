#!/bin/bash
echo 'SCRIPT'

exprot set FLASKN_ENV=dev
export set FLASK_APP=app.py

python -m flask run
