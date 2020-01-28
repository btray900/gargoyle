# gargoyle

This docker swarm is a containerized tool to check the [Openstack Security Guide](https://docs.openstack.org/security-guide/) checklist items in your environment.
Each possible check ends in a Pass/Fail result which is streamed to an Elasticsearch cluster for dashboard analysis. A reporting component
can produce PDF results for those who love hard copy.

# Pre-requisites

## Configure passwordless SSH login and sudo on hosts

Copy private key to ./engine/id_rsa before building the first time.

## Create docker volumes for any container to persist data

Default is a volume for elasticsearch and the engine /var/log

## Create passwords for Elastic X-Pack and other service users

### MAKE NEW PASSWORDS ON FIRST RUN OR IF g-esdata VOLUME DELETED, WHICH SHOULD RARELY BE DONE
docker exec -i g-elastic /bin/bash -c '/usr/share/elasticsearch/bin/elasticsearch-setup-passwords auto' | grep PASSWORD > .gargoyle.creds

python3 make_rc.py

# set env vars

source ./.gargoylerc



## Update sysctl or Elasticsearch may have issues

Check and set on docker host first to 262144 or higher

`sysctl vm.max_map_count`

`sudo sysctl -w vm.max_map_count=262144`

`sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf`

## Make your own certs if desired


# Update the sslGARGOYLE.cnf IP and/or names if needed

cd ./pki

# root ca key
openssl genrsa -out gargoyleRootCA.key.pem 2048

# root ca SAN cert
openssl req -new -x509 -extensions v3_ca -days 3650 -key gargoyleRootCA.key.pem -sha256 -out gargoyleRootCA.crt.pem -config sslGARGOYLE.cnf

# Common Name (e.g. server FQDN or YOUR name) []:gargoyleCA   <-- cannot match server certificate CommonName
# Email Address []:

# server key
openssl genrsa -out gargoyleServer.key.pem 2048

# create csr to be signed
openssl req -extensions v3_req -sha256 -new -key gargoyleServer.key.pem -out gargoyleServer.csr -config sslGARGOYLE.cnf

# Common Name (e.g. server FQDN or YOUR name) []:gargoyleServer   <--- cannot match CA certificate CommonName

# Create SAN certs signed by custom CA
openssl x509 -req -extensions v3_req -days 3650 -sha256 -in gargoyleServer.csr -CA gargoyleRootCA.crt.pem -CAkey gargoyleRootCA.key.pem -CAcreateserial -out gargoyleServer.crt.pem -extfile sslGARGOYLE.cnf

# Make client certs for db connections
openssl genrsa -out gargoyleClientDb.key.pem 2048

# create client csr
openssl req -extensions v3_req -sha256 -new -key gargoyleClientDb.key.pem -out gargoyleClientDb.csr -config sslGARGOYLE.cnf

# Common Name (e.g. server FQDN or YOUR name) []:gargoyleClientDb  <--- cannot match CA certificate CommmonName

#sign client csr
openssl x509 -req -extensions v3_req -days 1095 -sha256 -in gargoyleClientDb.csr -CA gargoyleRootCA.crt.pem -CAkey gargoyleRootCA.key.pem -CAcreateserial -out gargoyleClientDb.crt.pem -extfile sslGARGOYLE.cnf

# check certs OK
openssl verify -verbose -CAfile gargoyleRootCA.crt.pem gargoyleServer.crt.pem gargoyleClientDb.crt.pem
# gargoyleServer.crt.pem: OK
# gargoyleClientDb.crt.pem: OK

#Copy all the keys (except gargoyleRootCA.key.pem) to the containers

cp gargoyleRootCA.crt.pem ../api
cp gargoyleServer.crt.pem ../api
cp gargoyleServer.key.pem ../api
cp gargoyleClientDb.crt.pem ../api
cp gargoyleClientDb.key.pem ../api

cp gargoyleRootCA.crt.pem ../db
cp gargoyleServer.crt.pem ../db
cp gargoyleServer.key.pem ../db
cp gargoyleClientDb.crt.pem ../db
cp gargoyleClientDb.key.pem ../db

cp gargoyleRootCA.crt.pem ../elastic
cp gargoyleServer.crt.pem ../elastic
cp gargoyleServer.key.pem ../elastic
cp gargoyleClientDb.crt.pem ../elastic
cp gargoyleClientDb.key.pem ../elastic

cp gargoyleRootCA.crt.pem ../kibana
cp gargoyleServer.crt.pem ../kibana
cp gargoyleServer.key.pem ../kibana
cp gargoyleClientDb.crt.pem ../kibana
cp gargoyleClientDb.key.pem ../kibana

cp gargoyleRootCA.crt.pem ../engine
cp gargoyleServer.crt.pem ../engine
cp gargoyleServer.key.pem ../engine
cp gargoyleClientDb.crt.pem ../engine
cp gargoyleClientDb.key.pem ../engine

Update permissions for files in container

### Update paths for dev/prod environments

find ../gargoyle -type f -exec chmod 644 {} \;
find ../gargoyle -type d -exec chmod 755 {} \;
find ../gargoyle -type f -name "*.sh" -exec chmod 755 {} \;
find ../gargoyle -type f -name "*.py" -exec chmod 755 {} \;
chmod 755 ../gargoyle/python/proxychains-ng/configure

