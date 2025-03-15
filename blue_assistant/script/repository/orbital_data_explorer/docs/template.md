# orbital-data-explorer

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.

```yaml
include:::noref ../metadata.yaml
```
[metadata.yaml](../metadata.yaml)

🔥

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer .

@assets publish push .
```

set:::object_name orbital-data-explorer-2025-03-14-bp6m01

🔥

---

- [round 1](./round-1.md)