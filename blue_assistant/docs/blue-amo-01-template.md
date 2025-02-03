# blue-amo 1

set:::object_name blue-amo-2025-02-03-rvc2sl

details:::nodes
yaml:::get:::object_name:::script.nodes
details:::

details:::vars
yaml:::get:::object_name:::script.vars
details:::

```bash
@select blue-amo-$(@@timestamp)
@assistant script run - script=blue_amo .

@assets publish push .

@assistant build_README
```

details:::output
yaml:::get:::object_name:::output.script.nodes
details:::

assets:::get:::object_name/thumbnail-workflow.png

---

object:::blue-amo-2025-02-03-rvc2sl