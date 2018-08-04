FROM python:3.7

MAINTAINER aswwu.webmaster@wallawalla.edu

RUN apt-get update && \
    apt-get install -y --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install pipenv==2018.7.1 && \
    pip install uwsgi==2.0.17.1

RUN useradd -ms /bin/bash django
WORKDIR /home/django

COPY . django_server

WORKDIR /home/django/django_server
RUN pipenv install --system --deploy

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

USER django
CMD ["uwsgi", "--ini", "/home/django/django_server/uwsgi.ini"]
