#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py flush --no-input
python manage.py migrate

gunicorn configs.wsgi:application --bind 0.0.0.0:8000