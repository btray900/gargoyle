# gargoyle

The swarm is a containrized tool to check the [Openstack Security Guide](https://docs.openstack.org/security-guide/) checklist items in your environment.
Each check determines a Pass/Fail result which is streamed to an Elasticsearch cluster for dashboard analysis and a reporting function
allows for hard-copy PDF results.

# Pre-requisites

## Configure passwordless SSH login on hosts

Copy private key to ./engine/id_rsa before building the first time.

## Establish passwordless sudo for designated user on hosts

