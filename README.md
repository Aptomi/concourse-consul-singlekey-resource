# Concourse Hashicorp Consul Resource
[Concourse CI](http://concourse.ci) resource for watching and reacting to changes of a single key in Hashicorp [Consul](https://www.consul.io/).

A typical use case for this would be:
* create a resource instance that watches value of a given key in Consul
* when the value changes, generate a new resource version and run it through the pipeline
* retrieved key value is available to Concourse tasks
 
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

## `get`: Download the latest version
No parameters.

## Development
To build the docker image for the resource:
``` sh
python setup.py sdist
docker build -t <username>/concourse-consul-singlekey-resource .
```
