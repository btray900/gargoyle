FROM docker.elastic.co/elasticsearch/elasticsearch:6.8.6

COPY ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

RUN mkdir -p /opt/es_data
RUN mkdir -p /var/log/elasticsearch

COPY ./svtRootCA.crt.pem /usr/share/elasticsearch/config/
COPY ./svtRootCA.crt.pem /etc/ssl/certs/
COPY ./svtServer.crt.pem /usr/share/elasticsearch/config/
COPY ./svtServer.key.pem /usr/share/elasticsearch/config/

RUN chown -R elasticsearch:elasticsearch /opt/es_data
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch
RUN chown -R elasticsearch:elasticsearch /var/log/elasticsearch

VOLUME /opt/es_data

EXPOSE 9200 9300

USER elasticsearch

ENV ES_JAVA_OPTS -Des.http.cname_in_publish_address=true

CMD /usr/share/elasticsearch/bin/elasticsearch
