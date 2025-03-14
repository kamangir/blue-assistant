# orbital-data-explorer

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.

set:::object_name orbital-data-explorer-2025-02-04-6b8mp6

metadata:::get:::object_name:::output.script.nodes.researching_the_questions.output

```bash
@select orbital-data-explorer-$(@@timestamp)
@assistant script run - \
    script=orbital_data_explorer .

@assets publish push .

@assistant build_README
```


details:::output
metadata:::get:::object_name:::output.script.nodes
details:::

details:::workflow
assets:::get:::object_name/thumbnail-workflow.png
details:::

object:::get:::object_name