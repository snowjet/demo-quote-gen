# demo-quote-gen
Quote Generator

# Load balancing for A/B testing

```bash
oc new-project quote
oc project quote

oc create -f is_quote.yml
oc create -f build_quote.yml

oc new-app quote:v1 --name=ab-v1 --allow-missing-imagestream-tags=true
oc new-app quote:v2 --name=ab-v2 -e QUOTE_BACKEND=DB --allow-missing-imagestream-tags=true

oc create -f svc_ab.yml
oc create -f route_quote.yml

# create postgres database via the GUI
```

## Env

