# demo-quote-gen
Quote Generator

# Load balancing for A/B testing

```bash
oc apply -f ./oc_templates/build_*
```

```bash
oc apply -f ./oc_templates/dc_*
```

```bash
oc new-app quote:v1 --name=ab-v1
oc new-app quote:v2 --name=ab-v2 -e QUOTE_BACKEND=DB
```

```bash
oc apply -f ./oc_templates/route_*
```

## Env

