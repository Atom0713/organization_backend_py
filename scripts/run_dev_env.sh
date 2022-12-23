#!/bin/bash
echo "Activating DEBUG mode"
set FLASK_DEBUG=true

echo "Starting organization_backend_py"
poetry run --debug run
