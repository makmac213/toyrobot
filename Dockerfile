ARG PYTHON_IMG_VERSION=3.9.6

FROM python:${PYTHON_IMG_VERSION}-slim-buster as build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY ./ /app/toyrobot

RUN python -m pip install flake8

WORKDIR /app/toyrobot