#!/bin/bash

echo "Activating virtual env"
source venv_antalya_vandals_3_10/Scripts/activate

echo "Activating DEBUG mode"
set FLASK_DEBUG=true

echo "Starting organization_backend_py"
flask run
