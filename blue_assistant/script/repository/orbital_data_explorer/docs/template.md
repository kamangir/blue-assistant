# orbital-data-explorer 🔥

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/).

```yaml
include:::noref ../metadata.yaml
```
[metadata.yaml](../metadata.yaml)

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

🔥

---

- [round 1](./round-1.md)