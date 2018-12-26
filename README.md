# gargoyle

The swarm is a containerized tool to check the [Openstack Security Guide](https://docs.openstack.org/security-guide/) checklist items in your environment.
Each check determines a Pass/Fail result which is streamed to an Elasticsearch cluster for dashboard analysis. A reporting component
can produce PDF results for management types who love hard-copy.

# Pre-requisites

## Configure passwordless SSH login on hosts

Copy private key to ./engine/id_rsa before building the first time.

## Establish passwordless sudo for designated username on hosts.

