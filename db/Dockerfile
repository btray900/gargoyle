# gargoyle DB container

FROM mariadb:10.4.6

ARG dbuser
ARG dbpass
ARG dbdatabase

ARG cacrt
ARG servercrt
ARG serverkey
ARG clientcrt
ARG clientkey

COPY $cacrt /etc/ssl/certs/gRootCA_v2.crt
COPY $cacrt /etc/mysql
COPY $servercrt /etc/mysql/
COPY $serverkey /etc/mysql/
COPY $clientcrt /etc/mysql/
COPY $clientkey /etc/mysql/

COPY ./my.cnf /etc/mysql/

COPY osg.sql /docker-entrypoint-initdb.d/

RUN sed -i "s/xxxFAKEUSERxxx/$dbuser/g" /docker-entrypoint-initdb.d/osg.sql
RUN sed -i "s/xxxFAKEPASSWDxxx/$dbpass/g" /docker-entrypoint-initdb.d/osg.sql
RUN sed -i "s/xxxFAKEDATABASExxx/$dbdatabase/g" /docker-entrypoint-initdb.d/osg.sql

RUN sed -i "s/xxxCACRTxxx/$cacrt/g" /etc/mysql/my.cnf
RUN sed -i "s/xxxSERVERCRTxxx/$servercrt/g" /etc/mysql/my.cnf
RUN sed -i "s/xxxSERVERKEYxxx/$serverkey/g" /etc/mysql/my.cnf
RUN sed -i "s/xxxCLIENTCRTxxx/$clientcrt/g" /etc/mysql/my.cnf
RUN sed -i "s/xxxCLIENTKEYxxx/$clientkey/g" /etc/mysql/my.cnf

EXPOSE 3306
