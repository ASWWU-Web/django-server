FROM python:3.7

RUN apt-get update && \
    apt-get install -y && \
    pip install uwsgi && \
    pip install pipenv

RUN useradd -ms /bin/bash django
WORKDIR /home/django

COPY . django_server

RUN cd django_server && \
    pipenv install --system --deploy

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

USER django
CMD ["uwsgi", "--ini", "/home/django/django_server/uwsgi.ini"]
