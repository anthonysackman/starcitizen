# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends netcat

RUN apt-get install -y git

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install git+https://github.com/benoitc/gunicorn.git

COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/app/entrypoint.sh"]