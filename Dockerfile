FROM python:3.7

RUN apt-get update && \
    apt-get install -y && \
    pip install uwsgi && \
    pip install pipenv

COPY . /opt/django_server

WORKDIR /opt/django_server

RUN pipenv install --system --deploy

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

CMD ["uwsgi", "--ini", "/opt/django_server/uwsgi.ini"]
