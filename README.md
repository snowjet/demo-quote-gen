# demo-quote-gen
Quote Generator

# Load balancing for A/B testing

```bash
oc apply -f ./oc_templates/build_*

```bash
oc new-app quote:v1 --name=ab-v1
oc new-app quote:v2 --name=ab-v2
```

oc expose svc/ab-v1

oc edit route <route_name>
...
metadata:
  name: route-alternate-service
  annotations:
    haproxy.router.openshift.io/balance: roundrobin
spec:
  host: ab-example.my-project.my-domain
  to:
    kind: Service
    name: ab-example-a
    weight: 10
  alternateBackends:
  - kind: Service
    name: ab-example-b
    weight: 15

## Env

