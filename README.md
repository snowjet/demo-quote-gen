# demo-quote-gen

This is a simple Quote Generator that returns famous quotes from either a sqlite database, postgresql database or mysql (mariadb) database

For example:

```json
{
 "backend":"list",
 "quotes": {
    "name":"Benjamin Franklin",
    "quote":"Tell me and I forget.  Teach me and I remember.  Involve me and I learn."
}}
```


## CodeReady Workspaces

[![Contribute](images/factory-contribute.svg)](https://codeready-openshift-workspaces.apps-crc.testing/f?url=https://github.com/snowjet/demo-quote-gen)


## Pipelines (Tekton)

There are two Tekton pipelines offered by this applicaiton. One, which utilises a shared workspace and one that doesn't. This demonstrates both the benefit containers can provide to testing and the speed benefits of using workspaces. 

### Pipelines with Workspaces and Caching
The pipeline below only clones the repo once and pypi modules oncce. This is then used throughout the test and build processes to speed up deployments. The pipeline run **25%** quicker than the non-caching version.

![Pipeline](images/pipeline.png)

Install the pipelines with workspaces:
```bash
export PROJECT=<namespace>
oc apply -f ./oc_templates/pipeline-ws
```
### Pipelines with no caching
The pipeline below needs to clone and download the pypi modules 3 times, once for each pytest and again for the build. 

![Pipeline](images/pipeline-no-cache.png)

Install the pipelines without workspaces:
```bash 
export PROJECT=<namespace>
oc apply -f ./oc_templates/pipeline-no-ws
```

## create postgres database

```bash

export POSTGRESQL_DATABASE="quotes"
export POSTGRESQL_USER="user"
export POSTGRESQL_PASSWORD="`head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''`"

oc apply -f ./oc_templates/quotegen/secret_postgresql.yaml
oc apply -f ./oc_templates/quotegen/dc_postgresql.yaml
oc apply -f ./oc_templates/quotegen/svc_postgresql.yaml

```

## create application with postgres backend

```bash

oc apply -f ./oc_templates/quotegen/is_quotegen.yaml
oc apply -f ./oc_templates/quotegen/svc_quotegen.yaml
oc apply -f ./oc_templates/quotegen/dc_quotegen_db.yaml

oc expose svc/quotegen

```

## How to configure Kubernetes to load balancing for A/B testing

```bash

oc apply -f ./oc_templates/quotegen/is_quotegen.yaml
oc create -f ./oc_templates/quotegen/build_quotegen.yml

oc new-app quotegen:v1 --name=ab-v1 -e APP_HOME=quotegen --allow-missing-imagestream-tags=true
oc new-app quotegen:v2 --name=ab-v2 -e APP_HOME=quotegen -e QUOTE_BACKEND=DB --allow-missing-imagestream-tags=true

oc create -f svc_ab.yml
oc create -f route_quote.yml
```

