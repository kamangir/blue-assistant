# orbital-data-explorer ⏸️

Poking around [Orbital Data Explorer](https://ode.rsl.wustl.edu/) with an [AI DAG](../metadata.yaml).

```yaml
include:::noref ../metadata.yaml
```

## TLDR

- https://www.uahirise.org/catalog/
- https://pds.mcp.nasa.gov/portal/
- https://pds.nasa.gov/

## a run

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer,version=downloading_a_datacube .

@publish tar .

@assets publish extensions=png,push .
```

set:::object_name orbital-data-explorer-2025-03-16-xoo5vc

details:::output
metadata:::get:::object_name:::output
details:::

assets:::get:::object_name/thumbnail-workflow.png

object:::get:::object_name

## sample object

set:::PDS_object_name uahirise-ESP_086795_1970

assets:::blue-assistant/PDS/get:::object_name.png

object:::get:::object_name

🔥

⏸️

---

- [round 1](./round-1.md)