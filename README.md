# Concourse Hashicorp Consul Resource
[Concourse CI](http://concourse.ci) resource for watching changes of a single key in Hashicorp [Consul](https://www.consul.io/).

A typical use case for fetching new values would be:
* create a resource instance that watches value of a given key in Consul
* when the value changes, generate a new resource version and run it through the pipeline
* retrieved key value is available to Concourse tasks

This resource also supports writing values to Consul.
 
Docker image: https://hub.docker.com/r/aptomi/concourse-consul-singlekey-resource

## Source Configuration
* `host`: *Required* Hostname or IP address of Consul
* `port`: *Optional, default `443`* Consul port
* `scheme`: *Optional, default `https`* Consul scheme
* `token`: *Required* Consul token to use
* `key`: *Required* Name of the key in Consul to watch

### Example
``` yaml
resource_types:
- name: consul-singlekey
  type: docker-image
  source:
    repository: aptomi/concourse-consul-singlekey-resource

resources:
- name: consul
  type: consul-singlekey
  source:
    host: consul.mycompany.com
    token: f710a920-bb12-b356-ea1f-80f85f88f80b
    key: aaa/bbb/ccc/ddd
```

## `get`: Retrieve the latest value
No parameters.

## `put`: Store value
One of those parameters should be specified:
- `value` - string value to be stored in a given Consul key
- `value_file` - read value from this file and store it in a given Consul key

## Development
To build the docker image for the resource:
``` sh
python setup.py sdist
docker build -t <username>/concourse-consul-singlekey-resource .
```
