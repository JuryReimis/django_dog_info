FROM python:3.12-alpine3.21

RUN apk add postgresql-client build-base postgresql-dev

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password django-user

USER django-user

COPY django_dog_info /django_dog_info
WORKDIR /django_dog_info
EXPOSE 8000

ENV PYTHONUNBUFFERED=1
