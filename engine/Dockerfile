# main worker
# bt106c

FROM python:3.7
RUN apt-get update && apt-get -y install \
	openjdk-8-jdk \
        build-essential \
	git \
	curl \
	cron \
	nano
RUN pip install pyyaml paramiko elasticsearch fpdf requests bs4
RUN mkdir -p /gargoyle
RUN mkdir -p /var/log/gargoyle
RUN touch /etc/default/logstash
RUN mkdir -p /root/.ssh
COPY ./id_rsa /root/.ssh
COPY ./config /root/.ssh
RUN chmod 600 /root/.ssh/id_rsa
RUN curl -s -o /tmp/logstash-6.4.0.deb https://artifacts.elastic.co/downloads/logstash/logstash-6.4.0.deb
#COPY ./logstash-6.4.0.deb /tmp
COPY ./setup_dashboard.py /tmp
COPY ./check_health.sh /tmp
COPY ./hosts/ /tmp/
COPY ./dashboard/ /tmp/
COPY ./proxychains-ng/ /tmp/proxychains-ng/
COPY ./code/ /gargoyle/
RUN cd /tmp/proxychains-ng && ./configure --prefix=/usr --sysconfdir=/etc && make
COPY ./proxychains.conf /tmp
RUN dpkg -i /tmp/logstash-6.4.0.deb
VOLUME /var/log/gargoyle
COPY ./logstash.conf /etc/logstash/logstash.conf
CMD /tmp/check_health.sh && /usr/share/logstash/bin/logstash --verbose -f /etc/logstash/logstash.conf
