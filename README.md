# gargoyle

This docker swarm is a containerized tool to check the [Openstack Security Guide](https://docs.openstack.org/security-guide/) checklist items in your environment.
Each possible check ends in a Pass/Fail result which is streamed to an Elasticsearch cluster for dashboard analysis. A reporting component
can produce PDF results for those who love hard copy.

# Pre-requisites

## Configure passwordless SSH login and sudo on hosts

Copy private key to ./engine/id_rsa before building the first time.

## Update sysctl or Elasticsearch may have issues

Check and set on docker host first to 262144 or higher

`sysctl vm.max_map_count`

`sudo sysctl -w vm.max_map_count=262144`

`sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf`

