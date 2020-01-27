FROM mariadb:10.4.6

ARG dbpass

COPY ./gargoyleRootCA.crt.pem /etc/ssl/certs/
COPY ./gargoyleRootCA.crt.pem /etc/mysql/
COPY ./gargoyleServer.crt.pem /etc/mysql/
COPY ./gargoyleServer.key.pem /etc/mysql/
COPY ./gargoyleClientDb.crt.pem /etc/mysql/
COPY ./gargoyleClientDb.key.pem /etc/mysql/

COPY ./my.cnf /etc/mysql/

COPY osg.sql /docker-entrypoint-initdb.d/

RUN sed -i "s/xxxFAKEPASSWDxxx/$dbpass/g" /docker-entrypoint-initdb.d/osg.sql

EXPOSE 3306
