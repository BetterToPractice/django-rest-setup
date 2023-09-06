#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

celery -A configs worker -l info