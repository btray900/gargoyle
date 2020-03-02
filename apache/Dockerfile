# Gargoyle Frontend
# bt106c

FROM ubuntu:16.04

ARG frontuser
ARG frontpw

ARG cacrt
ARG servercrt
ARG serverkey
ARG clientcrt
ARG clientkey

RUN apt-get update && apt-get -y install software-properties-common

RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php

RUN apt-get update && apt-get -y install \
	apache2 \
        nano \
	php7.3 \
        curl \
	libapache2-mod-php7.3 \
	php7.3-mysql \
        php7.3-curl

COPY ./html/ /var/www/html/

COPY ./apache2.conf /etc/apache2/
COPY ./default-ssl.conf /etc/apache2/sites-available/

COPY ./gargoyle.htpasswd /var/www/.gargoyle.htpasswd

RUN mkdir -p /etc/apache2/certs
RUN mkdir -p /usr/local/share/ca-certificates/gargoyle

COPY $cacrt /usr/local/share/ca-certificates/gargoyle/gRootCA.crt

COPY $cacrt /etc/apache2/certs/
COPY $servercrt /etc/apache2/certs/
COPY $serverkey /etc/apache2/certs/
COPY $clientcrt /etc/apache2/certs/
COPY $clientkey /etc/apache2/certs/

RUN update-ca-certificates

EXPOSE 443

RUN a2dissite 000-default
RUN a2ensite default-ssl
RUN a2enmod ssl
RUN a2enmod headers

RUN /etc/init.d/apache2 stop

RUN htpasswd -bc /var/www/.gargoyle.htpasswd $frontuser $frontpw

ENV http_proxy=
ENV https_proxy=

CMD apachectl -k start -DFOREGROUND
