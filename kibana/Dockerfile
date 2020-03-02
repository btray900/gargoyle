FROM docker.elastic.co/kibana/kibana:6.8.6

ARG cacrt
ARG servercrt
ARG serverkey
ARG clientcrt
ARG clientkey

COPY $cacrt /etc/ssl/certs/
COPY $cacrt /usr/share/kibana/config/
COPY $servercrt /usr/share/kibana/config/
COPY $serverkey /usr/share/kibana/config/
COPY $clientcrt /usr/share/kibana/config/
COPY $clientkey /usr/share/kibana/config/

COPY ./kibana.yml /usr/share/kibana/config/kibana.yml

EXPOSE 5601

CMD /usr/share/kibana/bin/kibana

