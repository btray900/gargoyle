FROM docker.elastic.co/kibana/kibana:6.8.6

COPY ./kibana.yml /usr/share/kibana/config/kibana.yml

COPY ./gargoyleRootCA.crt.pem /usr/share/kibana/config/
COPY ./gargoyleServer.crt.pem /usr/share/kibana/config/
COPY ./gargoyleServer.key.pem /usr/share/kibana/config/

EXPOSE 5601

CMD /usr/share/kibana/bin/kibana

