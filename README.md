# gargoyle

This docker-compose app is a containerized tool to check the [Openstack Security Guide](https://docs.openstack.org/security-guide/) checklist items in your environment.
Each possible check ends in a Pass/Fail result which is streamed to an Elasticsearch cluster for dashboard analysis. A reporting component
can produce PDF results for those who love hard copy.

# Pre-requisites

## Configure passwordless SSH login and sudo on hosts

Copy private key to ./engine/id_rsa before building the first time.

## Create docker volumes for any container to persist data

Default is a volume for elasticsearch and the engine /var/log

## Create passwords for Elastic X-Pack and other service users

__Make new password for the first run, or if the elastic vlume gets deleted.__

`docker exec -i g-elastic /bin/bash -c '/usr/share/elasticsearch/bin/elasticsearch-setup-passwords auto' | grep PASSWORD > .gargoyle.creds`

*There won't be visible output, hit 'y' then 'enter' after a few seconds to continue password creation. Then run 'make_rc'*

`python3 make_rc.py`

## Set environment vars

`source ./.gargoylerc`

## Update sysctl or Elasticsearch may have issues

__Check and set on docker host settings__

`sysctl vm.max_map_count`

`sudo sysctl -w vm.max_map_count=262144`

`sudo echo "fs.file-max = 65535" >> /etc/sysctl.conf`

`sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf`

`sudo ulimit -n 65536`

*Add to /etc/security/limits.conf*

`* soft nofile 65535`

`* hard nofile 65535`


## Make your own certs if desired

### Update the sslGARGOYLE.cnf IP and/or names if needed

`openssl genrsa -out gRootCA_v2.key.pem 4096`

`openssl req -new -x509 -extensions v3_ca -days 3650 \
-key gRootCA_v2.key.pem -sha256 \
-out gRootCA_v2.crt.pem -config sslGARGOYLE.cnf`

`openssl genrsa -out gServer_v2.key.pem 4096`

`openssl req -extensions v3_req -sha256 -new \
-key gServer_v2.key.pem \
-out gServer_v2.csr \
-config sslGARGOYLE.cnf`

`openssl x509 -req -extensions v3_req -days 3650 \
-sha256 -in gServer_v2.csr -CA gRootCA_v2.crt.pem \
-CAkey gRootCA_v2.key.pem -CAcreateserial \
-out gServer_v2.crt.pem -extfile sslGARGOYLE.cnf`

`openssl genrsa -out gClientDb_v2.key.pem 4096`

`openssl req -extensions v3_req -sha256 -new \
-key gClientDb_v2.key.pem \
-out gClientDb_v2.csr -config sslGARGOYLE.cnf`

`openssl x509 -req -extensions v3_req -days 3650 -sha256 \
-in gClientDb_v2.csr -CA gRootCA_v2.crt.pem \
-CAkey gRootCA_v2.key.pem -CAcreateserial \
-out gClientDb_v2.crt.pem -extfile sslGARGOYLE.cnf`

`openssl verify -verbose -CAfile gRootCA_v2.crt.pem gServer_v2.crt.pem gClientDb_v2.crt.pem`


### Copy all the keys (except gargoyleRootCA.key.pem) to the containers

__Update permissions for files in container__

*Update paths for dev/prod environments*

`find ../gargoyle -type f -exec chmod 644 {} \;`

`find ../gargoyle -type d -exec chmod 755 {} \;`

`find ../gargoyle -type f -name "*.sh" -exec chmod 755 {} \;`

`find ../gargoyle -type f -name "*.py" -exec chmod 755 {} \;`

`chmod 755 ../gargoyle/engine/proxychains-ng/configure`

