FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY
ARG DJANGO_CORS_ORIGIN_WHITELIST

ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DJANGO_CORS_ORIGIN_WHITELIST $DJANGO_CORS_ORIGIN_WHITELIST

# RUN mkdir /quantumApi

WORKDIR /app
COPY requirements.txt /app/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py makemigrations
RUN python manage.py migrate
