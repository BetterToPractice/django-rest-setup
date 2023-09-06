FROM python:3.11.2-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY deploy/dev/entrypoint.sh /usr/src/app/deploy/entrypoint.sh
RUN chmod +x /usr/src/app/deploy/entrypoint.sh

COPY deploy/dev/start-app.sh /usr/src/app/deploy/start-app.sh
RUN chmod +x /usr/src/app/deploy/start-app.sh

COPY deploy/dev/start-beat.sh /usr/src/app/deploy/start-beat.sh
RUN chmod +x /usr/src/app/deploy/start-beat.sh

COPY deploy/dev/start-worker.sh /usr/src/app/deploy/start-worker.sh
RUN chmod +x /usr/src/app/deploy/start-worker.sh


COPY src/project .

ENTRYPOINT ["/usr/src/app/deploy/entrypoint.sh"]
