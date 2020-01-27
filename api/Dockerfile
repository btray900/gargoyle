FROM python:3.7

EXPOSE 5000

RUN mkdir -p /usr/local/share/ca-certificates/gargoyle

COPY ./gargoyleRootCA.crt.pem /usr/local/share/ca-certificates/gargoyle/gargoyleRootCA.crt
COPY ./gargoyleRootCA.crt.pem /app/
COPY ./gargoyleServer.crt.pem /app/
COPY ./gargoyleServer.key.pem /app/
COPY ./gargoyleClientDb.crt.pem /app/
COPY ./gargoyleClientDb.key.pem /app/

RUN update-ca-certificates

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY app.py /app

CMD python3 app.py
