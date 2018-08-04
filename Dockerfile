FROM python:3.7

MAINTAINER aswwu.webmaster@wallawalla.edu

RUN apt-get update && \
    apt-get install -y --no-install-recommends && \
    rm /var/lib/apt/lists/* \
    pip install pipenv~=2018.7

RUN useradd -ms /bin/bash django
WORKDIR /home/django

COPY . django_server

WORKDIR /home/django/django_server && \
    pipenv install --system --deploy

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

USER django
CMD ["uwsgi", "--ini", "/home/django/django_server/uwsgi.ini"]
