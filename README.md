Django Rest Setup
==========================================
[![Test & Deploy](https://github.com/BetterToPractice/django-rest-setup/actions/workflows/main.yml/badge.svg)](https://github.com/BetterToPractice/django-rest-setup/actions/workflows/main.yml)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/agung96tm/de1956fdfa1ea227f6e9cd051467b59a/raw/covbadge_django_rest_setup.json)

Getting started your django project using this repo.


How to Run
-----------------
#### Run Application
```commandline
docker-compose -f deploy/local/docker-compose.yml up -d -build

cd src/project

python manage.py migrate
python manage.py runserver
```

#### Run Worker & Scheduler
```commandline
cd src/project

celery -A configs beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A configs worker -l info
```
