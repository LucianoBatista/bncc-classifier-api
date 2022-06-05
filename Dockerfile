# base official image
FROM python:3.9-slim

LABEL maintainer='Education Group - BNCC'

# set working directory
WORKDIR /usr/src/app

ENV \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# copying requirements
COPY Pipfile* ./

RUN pip install -q --no-cache-dir \
  pipenv===2022.1.8 && \
  pipenv install --system

COPY ./ ./

COPY ./entrypoint.sh /sbin/entrypoint.sh

ENTRYPOINT ["/sbin/entrypoint.sh"]