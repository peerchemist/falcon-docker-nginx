FROM python:3.9-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y

COPY requirements.txt /

RUN pip3 install --no-cache-dir -r /requirements.txt

COPY app/ /app
WORKDIR /app

ENV APP_ENV docker

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "--timeout", "600", "main:app"]