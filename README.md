# demo-quote-gen

This is a simple Quote Generator that returns famous quotes from either a JSON list backend or from a postgresql database. 

For example:

```json
{
 "backend":"list",
 "name":"Benjamin Franklin",
 "quote":"Tell me and I forget.  Teach me and I remember.  Involve me and I learn."
}
```


## CodeReady Workspaces

[![Contribute](images/factory-contribute.svg)](https://codeready-openshift-workspaces.apps-crc.testing/f?url=https://github.com/snowjet/demo-quote-gen)

## How to configure Kubernetes to load balancing for A/B testing

```bash
oc new-project quote
oc project quote

oc create -f is_quote.yml
oc create -f build_quote.yml

oc new-app quote:v1 --name=ab-v1 --allow-missing-imagestream-tags=true
oc new-app quote:v2 --name=ab-v2 -e QUOTE_BACKEND=DB --allow-missing-imagestream-tags=true

oc create -f svc_ab.yml
oc create -f route_quote.yml
```

# create postgres database via the GUI


