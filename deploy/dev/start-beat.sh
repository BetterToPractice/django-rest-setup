#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

celery -A configs beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler