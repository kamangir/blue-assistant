# orbital-data-explorer

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.

🔥

```bash
@select orbital-data-explorer-$(@@timestamp)
@assistant script run - \
    script=orbital_data_explorer .

@assets publish push .

@assistant build_README
```

set:::object_name orbital-data-explorer-2025-02-03-vo3xjk

details:::output
yaml:::get:::object_name:::output.script.nodes
details:::

details:::workflow
assets:::get:::object_name/thumbnail-workflow.png
details:::

object:::get:::object_name