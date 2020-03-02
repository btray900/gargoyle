# gargoyle FLask API container

FROM python:3.7

ARG cacrt
ARG servercrt
ARG serverkey
ARG clientcrt
ARG clientkey

COPY $cacrt /etc/ssl/certs/
COPY $cacrt /app/
COPY $servercrt /app/
COPY $serverkey /app/
COPY $clientcrt /app/
COPY $clientkey /app/

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN mkdir -p /usr/local/share/ca-certificates/gargoyle

COPY $cacrt /usr/local/share/ca-certificates/gargoyle/gRootCA_v2.crt

RUN update-ca-certificates

RUN pip3 install -r requirements.txt

COPY app.py /app

ENV http_proxy=
ENV https_proxy=

CMD python3 app.py


