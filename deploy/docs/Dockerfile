FROM python:3.11.2-slim-buster

WORKDIR /usr/src/docs

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get clean \
  && apt-get install -y make

RUN pip install --upgrade pip
COPY deploy/docs/requirements.txt /usr/src/docs/requirements.txt
RUN pip install -r requirements.txt
RUN pip install sphinx-reload

COPY docs .

CMD sphinx-reload --host "0.0.0.0" --port "5500" .
