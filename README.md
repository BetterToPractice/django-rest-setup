Django Rest Setup
==========================================

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
