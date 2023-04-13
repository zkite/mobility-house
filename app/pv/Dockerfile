FROM python:3.9-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

RUN mkdir /tmp/pv_poc
WORKDIR /tmp/pv_poc

COPY . .

RUN pip install -r requirements/requirements.txt
