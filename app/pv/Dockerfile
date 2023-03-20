FROM python:3.9-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

RUN mkdir /tmp/mobility_house
WORKDIR /tmp/mobility_house

COPY . .

RUN pip install -r requirements/requirements.txt
