FROM python:3.12-alpine3.21

COPY requirements.txt /temp/requirements.txt
COPY django_dog_info /django_dog_info
WORKDIR /django_dog_info
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password django-user

USER django-user
