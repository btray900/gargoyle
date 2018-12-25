FROM mariadb:latest
ENV MYSQL_ROOT_PASSWORD xxxxFAKEPASSWDxxxx
COPY osg.sql /docker-entrypoint-initdb.d/
VOLUME /var/lib/mysql
EXPOSE 3306

