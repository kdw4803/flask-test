FROM python:3.5-slim

MAINTAINER fernando@linuxacademy.com

USER root

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install default-libmysqlclient-dev

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV NAME World

CMD ["python", "app.py"]