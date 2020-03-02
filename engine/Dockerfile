# main worker
# bt106c

FROM python:3.7

ARG cacrt
ARG servercrt
ARG serverkey
ARG clientcrt
ARG clientkey

RUN apt-get update && apt-get -y install \
	openjdk-11-jdk \
        build-essential \
	git \
        python3-pip \
	cron \
        jq \
	nano

RUN pip3 install pyyaml paramiko fpdf requests bs4
RUN pip3 install elasticsearch==6.3.1

RUN mkdir -p /gargoyle
RUN mkdir -p /var/log/gargoyle
RUN touch /etc/default/logstash
RUN mkdir -p /root/.ssh

RUN mkdir -p /usr/local/share/ca-certificates/gargoyle

COPY $cacrt /usr/local/share/ca-certificates/gargoyle/gRootCA_v2.crt

COPY $cacrt /etc/logstash/
COPY $servercrt /etc/logstash/
COPY $serverkey /etc/logstash/
COPY $clientcrt /etc/logstash/
COPY $clientkey /etc/logstash/

COPY ./id_rsa /root/.ssh
COPY ./config /root/.ssh

RUN chmod 600 /root/.ssh/id_rsa

RUN curl -s -o /tmp/logstash-6.8.6.deb https://artifacts.elastic.co/downloads/logstash/logstash-6.8.6.deb

COPY ./setup_dashboard.py /tmp
COPY ./check_health.py /tmp
COPY ./hosts/ /tmp/
COPY ./dashboard/ /tmp/
COPY ./proxychains-ng/ /tmp/proxychains-ng/
COPY ./code/ /gargoyle/

RUN cd /tmp/proxychains-ng && ./configure --prefix=/usr --sysconfdir=/etc && make

COPY ./proxychains.conf /tmp

RUN dpkg -i /tmp/logstash-6.8.6.deb

COPY ./logstash.conf /etc/logstash/logstash.conf

RUN mkdir -p /usr/share/logstash/config
COPY ./logstash.yml /usr/share/logstash/config/logstash.yml

RUN update-ca-certificates

CMD /usr/local/bin/python3 /tmp/check_health.py && /usr/share/logstash/bin/logstash --verbose -f /etc/logstash/logstash.conf
