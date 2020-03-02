FROM docker.elastic.co/elasticsearch/elasticsearch:6.8.6

ARG cacrt
ARG servercrt
ARG serverkey
ARG clientcrt
ARG clientkey

COPY $cacrt /etc/ssl/certs/
COPY $cacrt /usr/share/elasticsearch/config/
COPY $servercrt /usr/share/elasticsearch/config/
COPY $serverkey /usr/share/elasticsearch/config/
COPY $clientcrt /usr/share/elasticsearch/config/
COPY $clientkey /usr/share/elasticsearch/config/

COPY ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

RUN mkdir -p /opt/es_data
RUN mkdir -p /var/log/elasticsearch

RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch
RUN chown -R elasticsearch:elasticsearch /opt/es_data
RUN chown -R elasticsearch:elasticsearch /var/log/elasticsearch

VOLUME /opt/es_data

EXPOSE 9200 9300

USER elasticsearch

CMD /usr/share/elasticsearch/bin/elasticsearch

