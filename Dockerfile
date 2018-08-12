FROM python:3.7.0-alpine3.8

MAINTAINER aswwu.webmaster@wallawalla.edu

RUN apk add mariadb-dev && \
    apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers libffi-dev pcre pcre-dev && \
    pip install pipenv==2018.7.1 && \
    pip install uwsgi==2.0.17.1 && \
    set -e && \
    adduser -S django

WORKDIR /home/django

COPY . django_server

WORKDIR /home/django/django_server
RUN pipenv install --system --deploy

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

RUN apk del .build-deps

USER django
CMD ["uwsgi", "--ini", "/home/django/django_server/uwsgi.ini"]
